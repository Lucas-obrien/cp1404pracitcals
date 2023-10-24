from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
stratocaster = Guitar("Stratocaster", 2014, 350.15)

print(f"{gibson.name} - Expected 101. got {gibson.get_age()}")

print(f"{stratocaster.name} get_age() - Expected 9. got {stratocaster.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. got {gibson.is_vintage()}")
print(f"{stratocaster.name} is_vintage() - Expected False. got {stratocaster.is_vintage()}")

