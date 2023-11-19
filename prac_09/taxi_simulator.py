"""
Taxi trip simulator program

Estimated: 30 mins
Actual : 45 mins


"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"


def main():
    """A program that simulates taxi trips."""
    print("Let's drive!")
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = hail_taxi(current_taxi, taxis)
        elif menu_choice == "d":
            total_bill += calculate_taxi_trip(current_taxi)
        else:
            print("Invalid choice")
        print(f"Bill to date ${total_bill:.2f}")
        menu_choice = input(MENU).lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxi_rank(taxis)


def hail_taxi(current_taxi, taxis):
    """Choose a taxi to use."""
    print("Taxis available:")
    display_taxi_rank(taxis)
    try:
        current_taxi = taxis[int(input("Choose taxi: "))]
    except (IndexError, ValueError):
        print("Invalid taxi choice")
    return current_taxi


def calculate_taxi_trip(current_taxi):
    """Calculate taxi trip totals and return cost at end."""
    current_fare = 0
    if current_taxi:
        drive_distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(drive_distance)
        current_fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
        current_fare += current_fare
    else:
        print("You need to choose a taxi before you can drive")
    return current_fare


def display_taxi_rank(taxis):
    """Display the current taxis in a formatted list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
