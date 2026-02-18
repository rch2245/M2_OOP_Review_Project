"""
ShiftSupervisor Class - Inherits from Employee.
Adds annual salary and annual production bonus.
"""

from employee import Employee


class ShiftSupervisor(Employee):
    """Represents a shift supervisor who oversees production workers."""

    def __init__(self, name, employee_number, hire_date, annual_salary, annual_production_bonus):
        """
        Preconditions: Valid Employee args; annual_salary and annual_production_bonus
                       are positive floats
        Postconditions: ShiftSupervisor object initialized with all attributes
        """
        super().__init__(name, employee_number, hire_date)
        self._annual_salary = annual_salary
        self._annual_production_bonus = annual_production_bonus

    # ---- Getters and Setters ----

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._annual_salary = value
        else:
            raise ValueError("Annual salary must be positive.")

    @property
    def annual_production_bonus(self):
        return self._annual_production_bonus

    @annual_production_bonus.setter
    def annual_production_bonus(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._annual_production_bonus = value
        else:
            raise ValueError("Annual production bonus must be positive.")

    # ---- Display ----

    def __str__(self):
        """Returns a user-friendly string representation."""
        return (f"{super().__str__()}\n"
                f"  Annual Salary: ${self._annual_salary:,.2f}\n"
                f"  Annual Production Bonus: ${self._annual_production_bonus:,.2f}")

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return (f"ShiftSupervisor({self._name!r}, {self._employee_number!r}, "
                f"{self._hire_date!r}, {self._annual_salary!r}, {self._annual_production_bonus!r})")

    def print_shift_supervisor(self):
        """
        Preconditions: None
        Postconditions: Displays employee info plus salary and bonus
        """
        print(self.__str__())


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("ShiftSupervisor Class - Unit Tests")
    print("=" * 50)

    ss1 = ShiftSupervisor("Emily Carter", 3001, "05/01/2018", 65000.00, 5000.00)
    print("\nShift Supervisor 1:")
    ss1.print_shift_supervisor()
