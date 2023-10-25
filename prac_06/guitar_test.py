"""
guitar_test

Estimate - 45mins
Actual - 25mins

"""

from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
stratocaster = Guitar("Stratocaster", 2014, 350)
print(f"{gibson.name} - Expected 101. got {gibson.get_age()}")
print(f"{stratocaster.name} get_age() - Expected 9. got {stratocaster.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. got {gibson.is_vintage()}")
print(f"{stratocaster.name} is_vintage() - Expected False. got {stratocaster.is_vintage()}")

guitars = []  # could be written as list literal, leaving as is to look like final code
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512))

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
