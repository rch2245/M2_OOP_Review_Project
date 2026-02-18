"""
Shapes Hierarchy - Test Program (main.py)
Demonstrates polymorphism, getter/setter auto-recalculation,
and dynamic method resolution using a shapes list.
"""

from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    print("=" * 60)
    print("   Shapes Class Hierarchy - Test Program")
    print("=" * 60)

    # ---- Create a list of shapes (polymorphism) ----
    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(1, 1, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square"),
    ]

    # ---- Polymorphism check: loop and display each shape ----
    print("\n--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name} Area = {shape.area:.5f}")

    # ---- Getter/setter check with auto-recalculation ----
    print("\n--- Getter/setter check ---")

    # Circle: modify radius
    circle = shapes[0]  # Circle_1
    print(f"{circle.name} Current:  {circle.radius} {circle.area:.5f}")
    circle.radius = circle.radius * 2
    print(f"{circle.name} Doubled:  {circle.radius} {circle.area:.5f}")

    print()

    # Rectangle: modify length and width
    rect = shapes[2]  # Rectangle_1
    print(f"{rect.name} Current:  {rect.length} {rect.width} {rect.area:.0f}")
    rect.length = rect.length * 2
    rect.width = rect.width * 2
    print(f"{rect.name} Doubled:  {rect.length} {rect.width} {rect.area:.0f}")

    print()

    # Square: modify side
    sq = shapes[4]  # Square
    print(f"{sq.name} Current:  {sq.side} {sq.area:.0f}")
    sq.side = sq.side * 2
    print(f"{sq.name} Doubled:  {sq.side} {sq.area:.0f}")


if __name__ == "__main__":
    main()
