"""
Parking Ticket Simulation - Demonstration Program (main.py)
Tests 4 scenarios as specified in the project requirements.
"""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    print("=" * 60)
    print("   Parking Ticket Simulation - Test Scenarios")
    print("=" * 60)

    # ----------------------------------------------------------------
    # Scenario 1: A Car Is Parked Legally
    # ----------------------------------------------------------------
    print("\n--- Scenario 1: Car Parked Legally ---")
    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")

    ticket1 = officer1.inspect_car(car1, meter1)
    if ticket1 is None:
        print(f"  {car1.make} {car1.model} ({car1.license_number})")
        print(f"  Parked: {car1.minutes_parked} min | Purchased: {meter1.minutes_purchased} min")
        print("  Result: No ticket issued. Car is legally parked.")
    else:
        print(ticket1)

    # ----------------------------------------------------------------
    # Scenario 2: Illegally Parked (Less Than an Hour Over Time)
    # ----------------------------------------------------------------
    print("\n--- Scenario 2: Illegally Parked (<1 Hour Over) ---")
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")

    ticket2 = officer2.inspect_car(car2, meter2)
    if ticket2 is None:
        print("  No ticket issued. Car is legally parked.")
    else:
        print(ticket2)

    # ----------------------------------------------------------------
    # Scenario 3: Illegally Parked (Multiple Hours Over Time)
    # ----------------------------------------------------------------
    print("\n--- Scenario 3: Illegally Parked (Multiple Hours Over) ---")
    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")

    ticket3 = officer3.inspect_car(car3, meter3)
    if ticket3 is None:
        print("  No ticket issued. Car is legally parked.")
    else:
        print(ticket3)

    # ----------------------------------------------------------------
    # Scenario 4: Multiple Cars in a Parking Lot
    # ----------------------------------------------------------------
    print("\n--- Scenario 4: Multiple Cars in a Parking Lot ---")
    officer4 = PoliceOfficer("Sarah Green", "9999")

    # Create lists of cars and meters
    cars = [
        ParkedCar("Nissan", "Altima", "White", "JKL321", 60),
        ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80),
        ParkedCar("BMW", "X5", "Black", "BMW999", 500),
        ParkedCar("Mazda", "3", "Blue", "MAZ321", 45),
    ]

    meters = [
        ParkingMeter(60),
        ParkingMeter(60),
        ParkingMeter(60),
        ParkingMeter(60),
    ]

    for car, meter in zip(cars, meters):
        print(f"\nInspecting {car.make} {car.model} ({car.license_number}):")
        print(f"  Parked: {car.minutes_parked} min | Purchased: {meter.minutes_purchased} min")
        ticket = officer4.inspect_car(car, meter)
        if ticket is None:
            print("  Result: No ticket issued. Car is legally parked.")
        else:
            print(ticket)

    # ----------------------------------------------------------------
    # Summary Table
    # ----------------------------------------------------------------
    print("\n" + "=" * 60)
    print("   Test Data and Results Summary")
    print("=" * 60)
    print(f"{'Scenario':<12} {'Car':<30} {'Parked':<8} {'Meter':<8} {'Ticket':<8} {'Fine':<10} {'Officer'}")
    print("-" * 100)
    print(f"{'1':<12} {'Toyota Camry, Red, XYZ123':<30} {'30':<8} {'40':<8} {'No':<8} {'$0.00':<10} {'John Doe, 5678'}")
    print(f"{'2':<12} {'Honda Accord, Blue, ABC987':<30} {'70':<8} {'60':<8} {'Yes':<8} {'$25.00':<10} {'Jane Smith, 1234'}")
    print(f"{'3':<12} {'Ford Mustang, Black, LMN456':<30} {'190':<8} {'60':<8} {'Yes':<8} {'$45.00':<10} {'James Brown, 4321'}")
    print(f"{'4a':<12} {'Nissan Altima, White, JKL321':<30} {'60':<8} {'60':<8} {'No':<8} {'$0.00':<10} {'N/A'}")
    print(f"{'4b':<12} {'Chevy Malibu, Silver, QWE789':<30} {'80':<8} {'60':<8} {'Yes':<8} {'$25.00':<10} {'Sarah Green, 9999'}")
    print(f"{'4c':<12} {'BMW X5, Black, BMW999':<30} {'500':<8} {'60':<8} {'Yes':<8} {'$95.00':<10} {'Sarah Green, 9999'}")
    print(f"{'4d':<12} {'Mazda 3, Blue, MAZ321':<30} {'45':<8} {'60':<8} {'No':<8} {'$0.00':<10} {'N/A'}")


if __name__ == "__main__":
    main()
