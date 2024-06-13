# Function Definition: determine_eligibility takes dependent_age, household_income, and single_parent as parameters.
# Child Day Care (Form B202): Checks if the dependent is under 5 years old and calculates coverage based on household income. Adds 10% if it's a single-parent household.
# Extended Care (Form D303): Checks if the dependent is between 5 and under 13 years old and calculates coverage based on household income. Adds 10% if it's a single-parent household.
# Special Needs Care (Form Z452): Checks if the dependent is between 13 and under 22 years old and calculates coverage based on household income. Adds 10% if it's a single-parent household.
# Return: The function returns a list of dictionaries, each containing the form, eligibility, and coverage details for each applicable form.

def determine_eligibility(dependent_age, household_income, single_parent):
    benefits = []

    # Child Day Care (Form B202)
    if dependent_age < 5:
        coverage = 0
        if household_income <= 25000:
            coverage = 90
        elif 25000 < household_income <= 45000:
            coverage = 50
        
        if single_parent:
            coverage += 10

        benefits.append({
            "form": "B202",
            "coverage": coverage,
            "eligible": coverage > 0
        })

    # Extended Care (Form D303)
    if 5 <= dependent_age < 13:
        coverage = 0
        if household_income <= 20000:
            coverage = 90
        elif 20000 < household_income <= 50000:
            coverage = 50
        
        if single_parent:
            coverage += 10

        benefits.append({
            "form": "D303",
            "coverage": coverage,
            "eligible": coverage > 0
        })

    # Special Needs Care (Form Z452)
    if 13 <= dependent_age < 22:
        coverage = 0
        if household_income <= 20000:
            coverage = 90
        elif 20000 < household_income <= 50000:
            coverage = 50
        
        if single_parent:
            coverage += 10

        benefits.append({
            "form": "Z452",
            "coverage": coverage,
            "eligible": coverage > 0
        })

    return benefits


# Example
dependent_age = 14
household_income = 30000
single_parent = True

eligibility = determine_eligibility(dependent_age, household_income, single_parent)
for benefit in eligibility:
    print(f"Form: {benefit['form']}, Eligible: {benefit['eligible']}, Coverage: {benefit['coverage']}%")
