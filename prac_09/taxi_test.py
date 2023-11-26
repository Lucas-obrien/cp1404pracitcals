from taxi import Taxi


def run_test():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, ${my_taxi.get_fare():.2f}")


run_test()
