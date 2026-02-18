"""
Rectangle Class - Inherits from BasicShape.
Represents a rectangle with length and width.
Area is automatically recalculated when dimensions change.
"""

from basic_shape import BasicShape


class Rectangle(BasicShape):
    """Represents a rectangle shape."""

    def __init__(self, l, w, n="Rectangle"):
        """
        Preconditions: l, w are positive floats (length, width),
                       n is a string (shape name)
        Postconditions: Rectangle object initialized with area calculated
        """
        super().__init__()
        self._length = l
        self._width = w
        self._name = n
        self.calc_area()

    def calc_area(self):
        """
        Calculates the area of the rectangle (length * width).
        Postconditions: _area is updated in the base class
        """
        self._area = self._length * self._width

    @property
    def length(self):
        """Getter for _length."""
        return self._length

    @length.setter
    def length(self, value):
        """
        Setter for _length. Automatically recalculates area.
        Preconditions: value must be positive
        """
        self._length = value
        self.calc_area()

    @property
    def width(self):
        """Getter for _width."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for _width. Automatically recalculates area.
        Preconditions: value must be positive
        """
        self._width = value
        self.calc_area()


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("Rectangle Class - Unit Tests")
    print("=" * 50)

    r = Rectangle(10, 20, "Rectangle_1")
    print(f"\n{r.name}: length={r.length}, width={r.width}, area={r.area}")

    r.length = 20
    r.width = 40
    print(f"After doubling: length={r.length}, width={r.width}, area={r.area}")
