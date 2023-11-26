from unreliable_car import UnreliableCar


def run_tests():
    corolla = UnreliableCar("Corolla", 50, 50.0)
    corolla.drive(10)
    print(corolla)
    corolla.drive(20)
    print(corolla)
    corolla.drive(5)
    print(corolla)
    corolla.drive(5)
    print(corolla)
    corolla.drive(20)
    print(corolla)
    corolla.drive(5)
    print(corolla)
    corolla.drive(20)
    print(corolla)


run_tests()
