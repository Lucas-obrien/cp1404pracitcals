"""Guitar class
Estimate - 45mins
Actual - 25mins
"""


class Guitar:
    """Construct a guitar instance."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns formatted string, example: Gibson L-5 CES (1922) : $16,035.40."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return current year - guitar year."""
        return 2023 - self.year

    def is_vintage(self):
        """Return True or False if guitar age is > 50."""
        return self.get_age() > 50
