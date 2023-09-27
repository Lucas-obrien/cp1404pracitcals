"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Program that displays a menu, then converts either celsius or fahrenheit to the other."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            # temperature = convert_celsius_to_fahrenheit(celsius)
            # print(temperature)
            print(f"Result: {convert_celsius_to_fahrenheit(celsius):.2f} F")  # give the result from the function into
        elif choice == "F":                                                   # a variable for ease of reading
            fahrenheit = float(input("Fahrenheit: "))
            print(f"{convert_fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


main()
