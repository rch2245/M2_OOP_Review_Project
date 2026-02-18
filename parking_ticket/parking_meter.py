"""
ParkingMeter Class - Simulates a parking meter.
Stores the amount of time purchased.
"""


class ParkingMeter:
    """Represents a parking meter with purchased time."""

    def __init__(self, minutes_purchased=60):
        """
        Preconditions: minutes_purchased is a positive integer
        Postconditions: ParkingMeter object initialized
        """
        self._minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        """Getter for minutes_purchased."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        """
        Setter for minutes_purchased.
        Preconditions: value must be a positive integer (> 0)
        Postconditions: _minutes_purchased is updated
        Raises ValueError if value <= 0
        """
        if value <= 0:
            raise ValueError("Minutes purchased must be greater than 0.")
        self._minutes_purchased = value

    def __str__(self):
        """Returns a string representation of the parking meter."""
        return f"  Minutes Purchased: {self._minutes_purchased}"

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return f"ParkingMeter({self._minutes_purchased!r})"


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("ParkingMeter Class - Unit Tests")
    print("=" * 50)

    meter1 = ParkingMeter(40)
    print(f"\nMeter 1: {meter1.minutes_purchased} minutes")

    meter2 = ParkingMeter()
    print(f"Meter 2 (default): {meter2.minutes_purchased} minutes")

    print("\nSetting meter2 to 120 minutes:")
    meter2.minutes_purchased = 120
    print(f"  Minutes Purchased: {meter2.minutes_purchased}")

    print("\nAttempting to set minutes to 0:")
    try:
        meter2.minutes_purchased = 0
    except ValueError as e:
        print(f"  Error: {e}")
