"""
Square Class - Inherits from Rectangle.
Represents a square with a single side length.
Passes side as both length and width to Rectangle.
Area is automatically recalculated when side changes.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape (special case of Rectangle)."""

    def __init__(self, s, n="Square"):
        """
        Preconditions: s is a positive float (side length),
                       n is a string (shape name)
        Postconditions: Square object initialized with area calculated
        """
        self._side = s
        super().__init__(s, s, n)
        self.name = n  # ensure the name is set in BasicShape

    @property
    def side(self):
        """Getter for _side."""
        return self._side

    @side.setter
    def side(self, value):
        """
        Setter for _side. Automatically recalculates area by
        updating both length and width in the parent Rectangle.
        Preconditions: value must be positive
        """
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
