"""

estimate - 45mins
actual - 25mins

"""


from guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    current_guitar = Guitar(name, year, cost)
    guitars.append(current_guitar)
    print(f"{current_guitar} added\n")
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
