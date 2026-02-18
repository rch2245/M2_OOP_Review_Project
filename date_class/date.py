"""
Date Class - A wrapper around the datetime module.
Stores and validates dates, provides multiple string representations,
supports comparison and arithmetic-like operations, and allows
incrementing and decrementing dates.
"""

from datetime import date, timedelta
import calendar


class Date:
    """Custom Date class wrapping Python's datetime module."""

    # Month names for formatted output
    MONTH_NAMES = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    def __init__(self, month=1, day=1, year=1900):
        """
        Preconditions: month (1-12), day (1-last day of month), year (positive int)
        Postconditions: Date object initialized; defaults to 1/1/1900 if invalid
        """
        if self._is_valid_date(month, day, year):
            self._date = date(year, month, day)
        else:
            self._date = date(1900, 1, 1)

    # ---- Properties ----

    @property
    def month(self):
        return self._date.month

    @property
    def day(self):
        return self._date.day

    @property
    def year(self):
        return self._date.year

    # ---- Setters / Mutators ----

    def set_date(self, month, day, year):
        """
        Preconditions: month, day, year are integers
        Postconditions: Date is set if valid; otherwise defaults to 1/1/1900
        """
        if self._is_valid_date(month, day, year):
            self._date = date(year, month, day)
        else:
            self._date = date(1900, 1, 1)

    # ---- Validation Helpers ----

    @staticmethod
    def _is_valid_date(month, day, year):
        """Returns True if the given month, day, year form a valid date."""
        try:
            date(year, month, day)
            return True
        except (ValueError, TypeError):
            return False

    # ---- Leap Year ----

    def is_leap_year(self):
        """
        Preconditions: None
        Postconditions: Returns True if the object's year is a leap year
        """
        return calendar.isleap(self._date.year)

    @staticmethod
    def is_leap_year_static(year):
        """
        Preconditions: year is a positive integer
        Postconditions: Returns True if the given year is a leap year
        """
        return calendar.isleap(year)

    # ---- Last Day ----

    def last_day(self):
        """
        Preconditions: None
        Postconditions: Returns the last day of the current month/year
        """
        return calendar.monthrange(self._date.year, self._date.month)[1]

    @staticmethod
    def last_day_static(month, year):
        """
        Preconditions: month (1-12), year (positive integer)
        Postconditions: Returns the last day of the given month/year
        """
        return calendar.monthrange(year, month)[1]

    # ---- String Representations ----

    def format_1(self):
        """Format 1: MM/DD/YYYY (e.g., 12/25/2021)"""
        return self._date.strftime("%m/%d/%Y")

    def format_2(self):
        """Format 2: Month Day, Year (e.g., December 25, 2021)"""
        return self._date.strftime("%B %d, %Y")

    def format_3(self):
        """Format 3: Day Month Year (e.g., 25 December 2021)"""
        return self._date.strftime("%d %B %Y")

    def __str__(self):
        """Default string representation uses Format 2."""
        return self.format_2()

    def __repr__(self):
        return f"Date({self.month}, {self.day}, {self.year})"

    # ---- Operator Overloading ----

    def __add__(self, days):
        """
        Preconditions: days is a positive integer
        Postconditions: Returns a new Date object after adding days
        """
        new_date = self._date + timedelta(days=days)
        return Date(new_date.month, new_date.day, new_date.year)

    def __sub__(self, other):
        """
        Preconditions: other is a Date object
        Postconditions: Returns the number of days between two Date objects
        """
        if isinstance(other, Date):
            delta = self._date - other._date
            return abs(delta.days)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Date):
            return self._date == other._date
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Date):
            return self._date < other._date
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Date):
            return self._date <= other._date
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Date):
            return self._date > other._date
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Date):
            return self._date >= other._date
        return NotImplemented

    # ---- Increment / Decrement ----

    def increment(self):
        """
        Preconditions: None
        Postconditions: Advances the date by 1 day (handles month/year rollover)
        """
        new_date = self._date + timedelta(days=1)
        self._date = new_date

    def decrement(self):
        """
        Preconditions: None
        Postconditions: Decreases the date by 1 day (handles month/year rollover)
        """
        new_date = self._date - timedelta(days=1)
        self._date = new_date

    # ---- Alternative Constructor ----

    @classmethod
    def from_input(cls):
        """
        Preconditions: User provides month, day, year via console input
        Postconditions: Returns a new Date object from user input
        """
        try:
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            year = int(input("Enter year: "))
            return cls(month, day, year)
        except ValueError:
            print("Invalid input. Defaulting to 1/1/1900.")
            return cls()


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 60)
    print("Date Class - Unit Tests")
    print("=" * 60)

    # Test 1: Default constructor
    d1 = Date()
    print(f"\n1. Default constructor: {d1.format_1()}")

    # Test 2: Valid date, Format 2
    d2 = Date(4, 18, 2018)
    print(f"2. Valid date (Format 2): {d2.format_2()}")

    # Test 3: set_date and Format 3
    d3 = Date()
    d3.set_date(12, 25, 2021)
    print(f"3. set_date (Format 3): {d3.format_3()}")

    # Test 4: Invalid dates default to 1/1/1900
    print("\n--- Invalid Date Tests ---")
    invalid_dates = [(13, 45, 2018), (4, 31, 2000), (2, 29, 2009)]
    for m, d, y in invalid_dates:
        test = Date(m, d, y)
        print(f"   Date({m}, {d}, {y}) -> {test.format_1()}")

    # Test 5: Subtraction
    print("\n--- Subtraction Tests ---")
    d4 = Date(4, 18, 2014)
    d5 = Date(4, 10, 2014)
    print(f"   {d4.format_1()} - {d5.format_1()} = {d4 - d5} days")

    d6 = Date(2, 2, 2006)
    d7 = Date(11, 10, 2003)
    print(f"   {d6.format_1()} - {d7.format_1()} = {d6 - d7} days")

    # Test 6: Increment/decrement transitions
    print("\n--- Increment/Decrement Tests ---")
    d8 = Date(2, 29, 2008)
    print(f"   Start: {d8.format_1()}")
    d8.increment()
    print(f"   After increment: {d8.format_1()}")
    d8.decrement()
    print(f"   After decrement: {d8.format_1()}")

    d9 = Date(12, 31, 2024)
    print(f"\n   Start: {d9.format_1()}")
    d9.increment()
    print(f"   After increment: {d9.format_1()}")
    d9.decrement()
    print(f"   After decrement: {d9.format_1()}")

    # Test 7: Leap year
    print("\n--- Leap Year Tests ---")
    d10 = Date(1, 1, 2024)
    print(f"   2024 is leap year: {d10.is_leap_year()}")
    print(f"   2023 is leap year (static): {Date.is_leap_year_static(2023)}")

    # Test 8: Last day
    print("\n--- Last Day Tests ---")
    d11 = Date(2, 1, 2024)
    print(f"   Last day of Feb 2024: {d11.last_day()}")
    print(f"   Last day of Feb 2023 (static): {Date.last_day_static(2, 2023)}")

    # Test 9: Addition
    print("\n--- Addition Test ---")
    d12 = Date(1, 1, 2024)
    d13 = d12 + 366
    print(f"   {d12.format_1()} + 366 days = {d13.format_1()}")

    # Test 10: Comparison
    print("\n--- Comparison Tests ---")
    d14 = Date(1, 1, 2024)
    d15 = Date(12, 31, 2024)
    print(f"   {d14.format_1()} < {d15.format_1()}: {d14 < d15}")
    print(f"   {d14.format_1()} == {d14.format_1()}: {d14 == Date(1, 1, 2024)}")
