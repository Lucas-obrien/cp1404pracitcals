"""
Constructor for an Unreliable car

Estimate: 15 mins
Actual: 20 mins

"""

from car import Car
import random


class UnreliableCar(Car):
    """Constructor for an UnreliableCar"""

    def __init__(self, name, fuel, reliability):
        """Initialise a Car, then give reliability."""
        Car.__init__(self, name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Check to see if car starts, then drive"""
        if self.reliability < float(random.randint(0, 100)):
            distance = 0
        else:
            super().drive(distance)
        return distance

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


