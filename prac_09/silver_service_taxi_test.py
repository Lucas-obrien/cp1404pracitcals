from silver_service_taxi import SilverServiceTaxi


def run_tests():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.start_fare()
    hummer.drive(18)
    print(hummer)
    print(f"${hummer.get_fare():.2f}")


run_tests()
