"""
ParkingTicket Class - Simulates a parking ticket.
Calculates fines and reports details about the violation.
"""

import math


class ParkingTicket:
    """Represents a parking ticket issued for illegal parking."""

    def __init__(self, car, officer, illegal_minutes):
        """
        Preconditions: car is a ParkedCar object, officer is a PoliceOfficer object,
                       illegal_minutes is a positive integer
        Postconditions: ParkingTicket created with fine calculated
        """
        self.car = car                          # composition - retains reference
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        """
        Calculates the fine for illegal parking.
        Formula: $25 for the first hour or part of an hour,
                 plus $10 for each additional hour or part.
        Preconditions: illegal_minutes > 0
        Postconditions: Returns the total fine as a float
        """
        total_hours = math.ceil(self.illegal_minutes / 60)
        fine = 25.00  # first hour or part
        if total_hours > 1:
            fine += (total_hours - 1) * 10.00  # each additional hour or part
        return fine

    def __str__(self):
        """Returns a formatted string displaying the ticket details."""
        return (
            f"{'=' * 40}\n"
            f"       PARKING TICKET\n"
            f"{'=' * 40}\n"
            f"  Car Details:\n"
            f"    Make: {self.car.make}\n"
            f"    Model: {self.car.model}\n"
            f"    Color: {self.car.color}\n"
            f"    License: {self.car.license_number}\n"
            f"  Violation:\n"
            f"    Illegal Minutes: {self.illegal_minutes}\n"
            f"    Fine: ${self.fine:.2f}\n"
            f"  Issued By:\n"
            f"    Officer: {self.officer_name}\n"
            f"    Badge: {self.badge_number}\n"
            f"{'=' * 40}"
        )

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return f"ParkingTicket({self.car!r}, {self.officer_name!r}, {self.illegal_minutes!r})"


# ---- Unit Tests ----
if __name__ == "__main__":
    from parked_car import ParkedCar
    from police_officer import PoliceOfficer

    print("=" * 50)
    print("ParkingTicket Class - Unit Tests")
    print("=" * 50)

    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    officer = PoliceOfficer("Jane Smith", "1234")
    ticket = ParkingTicket(car, officer, 10)
    print(f"\nFine for 10 illegal minutes: ${ticket.fine:.2f}")
    print(ticket)

    # Test multi-hour fine
    car2 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    ticket2 = ParkingTicket(car2, officer, 130)
    print(f"\nFine for 130 illegal minutes: ${ticket2.fine:.2f}")
