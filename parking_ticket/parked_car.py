"""
ParkedCar Class - Simulates a parked car.
Stores identifying information and how long it has been parked.
"""


class ParkedCar:
    """Represents a parked car with make, model, color, license, and minutes parked."""

    def __init__(self, make, model, color, license_number, minutes_parked=60):
        """
        Preconditions: make, model, color, license_number are strings;
                       minutes_parked is a positive integer
        Postconditions: ParkedCar object initialized with the given attributes
        """
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = minutes_parked  # private attribute

    @property
    def minutes_parked(self):
        """Getter for minutes_parked."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        """
        Setter for minutes_parked.
        Preconditions: value must be a positive integer (> 0)
        Postconditions: _minutes_parked is updated
        Raises ValueError if value <= 0
        """
        if value <= 0:
            raise ValueError("Minutes parked must be greater than 0.")
        self._minutes_parked = value

    def __str__(self):
        """Returns a string representation of the parked car."""
        return (f"  Make: {self.make}\n"
                f"  Model: {self.model}\n"
                f"  Color: {self.color}\n"
                f"  License: {self.license_number}\n"
                f"  Minutes Parked: {self._minutes_parked}")


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("ParkedCar Class - Unit Tests")
    print("=" * 50)

    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    print("\nCar 1:")
    print(car1)

    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987")
    print("\nCar 2 (default minutes):")
    print(car2)

    # Test setter validation
    print("\nSetting car2 minutes to 90:")
    car2.minutes_parked = 90
    print(f"  Minutes Parked: {car2.minutes_parked}")

    print("\nAttempting to set minutes to -5:")
    try:
        car2.minutes_parked = -5
    except ValueError as e:
        print(f"  Error: {e}")
