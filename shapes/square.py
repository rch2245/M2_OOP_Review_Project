"""
Square Class - Inherits from Rectangle.
Represents a square with a single side length.
Passes side as both length and width to Rectangle.
Area is automatically recalculated when side changes.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape (special case of Rectangle)."""

    def __init__(self, side, name="Square"):
        """
        Preconditions: side is a positive float (side length),
                       name is a string (shape name)
        Postconditions: Square object initialized with area calculated
        """
        self._side = side
        super().__init__(side, side, name)
        self.name = name  # ensure the name is set in BasicShape

    def __str__(self):
        """Returns a user-friendly string representation."""
        return f"{self._name}: Side={self._side}, Area={self._area:.5f}"

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return f"Square({self._side!r}, {self._name!r})"

    @property
    def side(self):
        """Getter for _side."""
        return self._side

    @side.setter
    def side(self, value):
        """
        Setter for _side. Validates positive value and automatically
        recalculates area by updating both length and width.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be a number.")
        if value <= 0:
            raise ValueError("Side must be positive.")
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("Square Class - Unit Tests")
    print("=" * 50)

    sq = Square(10, "Square")
    print(f"\n{sq.name}: side={sq.side}, area={sq.area}")

    sq.side = 20
    print(f"After doubling side: side={sq.side}, area={sq.area}")
