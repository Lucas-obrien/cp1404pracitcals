from car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        Car.__init__(self, name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < float(random.randint(0, 100)):
            distance = 0
        else:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


