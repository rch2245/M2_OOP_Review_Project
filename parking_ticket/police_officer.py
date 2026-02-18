"""
PoliceOfficer Class - Simulates a police officer inspecting parked cars.
Examines a ParkedCar and ParkingMeter to determine if a ticket should be issued.
"""

from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represents a police officer who inspects cars and issues tickets."""

    def __init__(self, name, badge_number):
        """
        Preconditions: name and badge_number are strings
        Postconditions: PoliceOfficer object initialized
        """
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
        """
        Examines a ParkedCar and ParkingMeter to determine if the car
        is illegally parked.

        Preconditions: parked_car is a ParkedCar object,
                       parking_meter is a ParkingMeter object
        Postconditions: Returns a ParkingTicket if illegally parked,
                        or None if legally parked
        """
        if parked_car.minutes_parked > parking_meter.minutes_purchased:
            illegal_minutes = parked_car.minutes_parked - parking_meter.minutes_purchased
            return ParkingTicket(parked_car, self, illegal_minutes)
        return None

    def __str__(self):
        """Returns a string representation of the officer."""
        return f"  Officer: {self.name}, Badge: {self.badge_number}"


# ---- Unit Tests ----
if __name__ == "__main__":
    from parked_car import ParkedCar
    from parking_meter import ParkingMeter

    print("=" * 50)
    print("PoliceOfficer Class - Unit Tests")
    print("=" * 50)

    officer = PoliceOfficer("John Doe", "5678")
    print(f"\n{officer}")

    # Legal parking
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    result = officer.inspect_car(car, meter)
    print(f"\nInspecting Toyota Camry (30 min parked, 40 min purchased):")
    if result is None:
        print("  No violation. Car is legally parked.")
    else:
        print(result)

    # Illegal parking
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    result2 = officer.inspect_car(car2, meter2)
    print(f"\nInspecting Honda Accord (70 min parked, 60 min purchased):")
    if result2 is None:
        print("  No violation. Car is legally parked.")
    else:
        print(result2)
