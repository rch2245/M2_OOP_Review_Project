"""
Employee Class - Base class for the Factory Workers hierarchy.
Stores basic employee information: name, employee number, and hire date.
"""


class Employee:
    """Base class representing a generic employee."""

    def __init__(self, name, employee_number, hire_date):
        """
        Preconditions: name is a non-empty string, employee_number is int or str,
                       hire_date is a string or tuple (month, day, year)
        Postconditions: Employee object initialized with the given attributes
        """
        self._name = name
        self._employee_number = employee_number
        self._hire_date = hire_date

    # ---- Getters and Setters ----

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def employee_number(self):
        return self._employee_number

    @employee_number.setter
    def employee_number(self, value):
        if not isinstance(value, (int, str)):
            raise TypeError("Employee number must be an int or string.")
        self._employee_number = value

    @property
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value):
        if not isinstance(value, (str, tuple)):
            raise TypeError("Hire date must be a string or tuple.")
        self._hire_date = value

    # ---- Display ----

    def __str__(self):
        """Returns a user-friendly string representation."""
        return (f"  Name: {self._name}\n"
                f"  Employee Number: {self._employee_number}\n"
                f"  Hire Date: {self._hire_date}")

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return f"Employee({self._name!r}, {self._employee_number!r}, {self._hire_date!r})"

    def print_employee(self):
        """
        Preconditions: None
        Postconditions: Displays all employee attributes to console
        """
        print(self.__str__())


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("Employee Class - Unit Tests")
    print("=" * 50)

    e1 = Employee("Alice Johnson", 1001, "03/15/2020")
    print("\nEmployee 1:")
    e1.print_employee()

    e2 = Employee("Bob Smith", 1002, (6, 1, 2019))
    print("\nEmployee 2:")
    e2.print_employee()

    # Test setters
    e1.name = "Alice Williams"
    e1.employee_number = 2001
    e1.hire_date = "04/20/2021"
    print("\nEmployee 1 (after updates):")
    e1.print_employee()
