"""Module docstring

estimation - 30 mins
actual -

"""


class ProgrammingLanguage:
    """Constructs programming language data fields"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.reflection

