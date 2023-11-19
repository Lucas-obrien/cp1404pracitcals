"""Module docstring

estimation - 30 mins
actual - 16 mins

"""


class ProgrammingLanguage:
    """Constructs programming language data fields."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True or False if programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return constructed string of name, typing, reflection and first appearance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
