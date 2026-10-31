# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")
        self.width = width
        self.height = height

    def is_square(self):
        """Return True if the rectangle is a square, False otherwise."""
        return self.width == self.height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)