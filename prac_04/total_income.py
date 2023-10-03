"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Print report of individual incomes per month and a sum of total income per month"""
    print("\nIncome Report\n-------------")
    for month in range(1, number_of_months + 1):
        print(f"Month {month:>2} - Income: ${incomes[month-1]:10.2f} Total: ${sum(incomes[0:month]):10.2f}")


main()
