"""
ProductionWorker Class - Inherits from Employee.
Adds shift (1=day, 2=night) and hourly pay rate.
"""

from employee import Employee


class ProductionWorker(Employee):
    """Represents a production worker on the factory floor."""

    def __init__(self, name, employee_number, hire_date, shift, hourly_pay_rate):
        """
        Preconditions: Valid Employee args; shift is 1 (day) or 2 (night);
                       hourly_pay_rate is a positive float
        Postconditions: ProductionWorker object initialized with all attributes
        """
        super().__init__(name, employee_number, hire_date)
        self._shift = shift
        self._hourly_pay_rate = hourly_pay_rate

    # ---- Getters and Setters ----

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, value):
        # Precondition: value must be 1 or 2
        if value in (1, 2):
            self._shift = value
        else:
            raise ValueError("Shift must be 1 (day) or 2 (night).")

    @property
    def hourly_pay_rate(self):
        return self._hourly_pay_rate

    @hourly_pay_rate.setter
    def hourly_pay_rate(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._hourly_pay_rate = value
        else:
            raise ValueError("Hourly pay rate must be positive.")

    # ---- Display ----

    def print_production_worker(self):
        """
        Preconditions: None
        Postconditions: Displays employee info plus shift and pay rate
        """
        self.print_employee()
        shift_name = "Day" if self._shift == 1 else "Night"
        print(f"  Shift: {shift_name}")
        print(f"  Hourly Pay Rate: ${self._hourly_pay_rate:.2f}")


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("ProductionWorker Class - Unit Tests")
    print("=" * 50)

    pw1 = ProductionWorker("Carlos Diaz", 2001, "01/10/2021", 1, 18.50)
    print("\nProduction Worker 1:")
    pw1.print_production_worker()

    pw2 = ProductionWorker("Diana Prince", 2002, "07/22/2022", 2, 22.75)
    print("\nProduction Worker 2:")
    pw2.print_production_worker()
