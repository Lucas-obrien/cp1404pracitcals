"""
Fancy taxi constructor

Estimation: 20 mins
Actual: 15 mins

"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Constructor for fancy taxis."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Construct a fancy taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the fancy taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """String representation of the fancy taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
