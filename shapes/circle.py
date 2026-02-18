"""
Circle Class - Inherits from BasicShape.
Represents a circle with center coordinates and radius.
Area is automatically recalculated when radius changes.
"""

import math
from basic_shape import BasicShape


class Circle(BasicShape):
    """Represents a circle shape."""

    def __init__(self, x, y, r, n="Circle"):
        """
        Preconditions: x, y are floats (center coordinates),
                       r is a positive float (radius),
                       n is a string (shape name)
        Postconditions: Circle object initialized with area calculated
        """
        super().__init__()
        self._x_center = x
        self._y_center = y
        self._radius = r
        self._name = n
        self.calc_area()

    def calc_area(self):
        """
        Calculates the area of the circle (pi * r^2).
        Postconditions: _area is updated in the base class
        """
        self._area = math.pi * self._radius ** 2

    @property
    def x_center(self):
        """Getter for _x_center."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        """Setter for _x_center."""
        self._x_center = value

    @property
    def y_center(self):
        """Getter for _y_center."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        """Setter for _y_center."""
        self._y_center = value

    @property
    def radius(self):
        """Getter for _radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Setter for _radius. Automatically recalculates area.
        Preconditions: value must be positive
        """
        self._radius = value
        self.calc_area()


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("Circle Class - Unit Tests")
    print("=" * 50)

    c = Circle(0, 0, 4, "Circle_1")
    print(f"\n{c.name}: radius={c.radius}, area={c.area:.5f}")

    c.radius = 8
    print(f"After doubling radius: radius={c.radius}, area={c.area:.5f}")
