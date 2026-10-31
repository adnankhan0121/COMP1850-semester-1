# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """Create a Person with the given name and date of birth."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name cannot be an empty string")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercased initials of the person's name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return True if today is the person's birthday, False otherwise."""
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day
    