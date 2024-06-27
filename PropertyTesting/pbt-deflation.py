import random
import os
import anthropic

random.seed(100) # For reproudicibility; remove to get randomness

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

base_cpi = 138.2

def compute_std_deduction(tax_year, cpi_previous_year):
	message = client.messages.create(
	    model="claude-3-opus-20240229",
	    max_tokens=2000,
	    temperature=0,
	    system="You are an expert legal reasoning system, capable of reading legal statutes and applying them to given scenarios by identifying the correct subset of sections that apply to the particular situation.\n\nIn this conversation, we are only going to refer the following statutes. Do not use your knowledge of any other piece of legislation not provided in this conversation. If any undefined section is referenced in a question, please refuse to answer the question. The statutes referenced in this conversation are as follows:\n\n```\n§63. Taxable income defined\n\n...\n\n(b) Individuals who do not itemize their deductions\n\n  In the case of an individual who does not elect to itemize his deductions for the taxable year, for purposes of this subtitle, the term “taxable income” means adjusted gross income, minus—\n  \n  (1) the standard deduction,\n\n  ...\n\n(c) Standard deduction\n\n    (1) In general\n\n    Except as otherwise provided in this subsection, the term \"standard deduction\" means the sum of-\n\n        (A) the basic standard deduction, and\n\n        (B) the additional standard deduction.\n\n    (2) Basic standard deduction\n\n    For purposes of paragraph (1), the basic standard deduction is-\n\n        (A) 200 percent of the dollar amount in effect under subparagraph (C) for the taxable year in the case of-\n\n            (i) a joint return, or\n\n            (ii) a surviving spouse (as defined in section 2(a)),\n\n        (B) $4,400 in the case of a head of household (as defined in section 2(b)), or\n\n        (C) $3,000 in any other case.\n\n    (3) Additional standard deduction for aged and blind\n\n    For purposes of paragraph (1), the additional standard deduction is the sum of each additional amount to which the taxpayer is entitled under subsection (f).\n\n    (4) Adjustments for inflation\n\n        In the case of any taxable year beginning in a calendar year after 1988, each dollar amount contained in paragraph (2)(B), (2)(C), or (5) or subsection (f) shall be increased by an amount equal to— \n        \n        ...\n\n    (7) Special rules for taxable years 2018 through 2025\n\n    In the case of a taxable year beginning after December 31, 2017, and before January 1, 2026-\n\n    (A) Increase in standard deduction\n\n        Paragraph (2) shall be applied—\n\n        (i) by substituting “$18,000” for “$4,400” in subparagraph (B), and\n\n        (ii) by substituting “$12,000” for “$3,000” in subparagraph (C).\n        \n    (B) Adjustment for inflation\n            \n        (i) In general\n    \n        Paragraph (4) shall not apply to the dollar amounts contained in paragraphs (2)(B) and (2)(C).\n\n        (ii) Adjustment of increased amounts\n        \n            In the case of a taxable year beginning after 2018, the $18,000 and $12,000 amounts in subparagraph (A) shall each be increased by an amount equal to—\n            \n            (I) such dollar amount, multiplied by\n            \n            (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting “2017” for “2016” in subparagraph (A)(ii) thereof.\n\n            If any increase under this clause is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50.\n\n    Paragraph (2) shall be applied-\n\n        (i) by substituting \"$18,000\" for \"$4,400\" in subparagraph (B), and\n\n        (ii) by substituting \"$12,000\" for \"$3,000\" in subparagraph (C).\n\n...\n\n(f) Aged or blind additional amounts\n\n  (1) Additional amounts for the aged\n  \n    The taxpayer shall be entitled to an additional amount of $600—\n    \n    (A) for himself if he has attained age 65 before the close of his taxable year, and\n    \n    (B) for the spouse of the taxpayer if the spouse has attained age 65 before the close of the taxable year and an additional exemption is allowable to the taxpayer for such spouse under section 151(b).\n\n  ...\n\n§1. Tax imposed\n\n...\n\n(f) Adjustments in tax tables so that inflation will not result in tax increases\n\n    ...\n\n    (3) Cost-of-living adjustment\n\n        For purposes of this subsection—\n\n        (A) In general\n\n            The cost-of-living adjustment for any calendar year is the percentage (if any) by which—\n\n            (i) the C-CPI-U for the preceding calendar year, exceeds\n\n            (ii) the CPI for calendar year 2016, multiplied by the amount determined under subparagraph (B).\n\n        (B) Amount determined\n\n            The amount determined under this clause is the amount obtained by dividing—\n\n            (i) the C-CPI-U for calendar year 2016, by\n\n            (ii) the CPI for calendar year 2016.\n\n        (C) Special rule for adjustments with a base year after 2016\n            \n        For purposes of any provision of this title which provides for the substitution of a year after 2016 for “2016” in subparagraph (A)(ii), subparagraph (A) shall be applied by substituting “the C-CPI-U for calendar year 2016” for “the CPI for calendar year 2016” and all that follows in clause (ii) thereof.\n\n    (4) CPI for any calendar year\n        \n    For purposes of paragraph (3), the CPI for any calendar year is the average of the Consumer Price Index as of the close of the 12-month period ending on August 31 of such calendar year.\n\n    (6) C-CPI-U\n    \n        ...\n\n        (B) Determination for calendar year\n    \n        The C-CPI-U for any calendar year is the average of the C-CPI-U as of the close of the 12-month period ending on August 31 of such calendar year.\n\n        ...\n\n§151. Allowance of deductions for personal exemptions\n\n    ...\n\n    (b) Taxpayer and spouse\n    \n    An exemption of the exemption amount for the taxpayer; and an additional exemption of the exemption amount for the spouse of the taxpayer if a joint return is not made by the taxpayer and his spouse, and if the spouse, for the calendar year in which the taxable year of the taxpayer begins, has no gross income and is not the dependent of another taxpayer.\n\n    ...\n\n```",
	    messages=[
	        {
	            "role": "user",
	            "content": [
	                {
	                    "type": "text",
	                    "text": f"Alice is filing taxes as a single person for the year {tax_year}. Alice was born on 1/1/1981. Alice does not itemize her deductions and does not qualify for any deductions other than the standard deduction. What is the standard deduction available to her?\n\nThe average C-CPI-U values for calendar year 2017 is {base_cpi} and for the year before {tax_year} is {cpi_previous_year}.\n\nLet's think step by step. End your response with the final dollar amount on a single line."
	                }
	            ]
	        }
	    ]
	)
	response = message.content[0]
	assert(response.type == "text")
	dollar_amount = response.text.strip().split("\n")[-1]
	return int(dollar_amount.replace('$', '').replace(',', ''))

# Random fuzzing
iter = 1
while True:
	X = random.randint(2018, 2024)
	Y = random.randint(X, 2025)
	Ix = random.randrange(100, 200)
	Iy = random.randrange(100, 200)
	Dx = compute_std_deduction(X, Ix)
	Dy = compute_std_deduction(Y, Iy)
	print(f"iter={iter}, X={X}, Ix={Ix}, Y={Y}, Iy={Iy}, Dx={Dx}, Dy={Dy}, ")
	if Dy < Dx:
		# Standard deduction in year Y has reduced compared to that in year X
		print("Property violation found!")
		break
	iter = iter + 1

