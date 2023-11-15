"""

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
            current_taxi = hail_taxi(current_taxi, taxis, total_bill)
        elif menu_choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid choice")
        print(f"Bill to date ${total_bill:.2f}")
        menu_choice = input(MENU).lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxi_rank(taxis)


def hail_taxi(current_taxi, taxis, total_bill):
    print("Taxis available:")
    display_taxi_rank(taxis)
    try:
        current_taxi = taxis[int(input("Choose taxi: "))]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(current_taxi, total_bill):
    if current_taxi is not None:
        drive_distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(drive_distance)
        current_fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
        total_bill += current_fare
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def display_taxi_rank(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
