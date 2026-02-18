"""
TeamLeader Class - Inherits from ProductionWorker.
Adds monthly bonus, required training hours, and attended training hours.
"""

from production_worker import ProductionWorker


class TeamLeader(ProductionWorker):
    """Represents a team leader who supervises a group of production workers."""

    def __init__(self, name, employee_number, hire_date, shift, hourly_pay_rate,
                 monthly_bonus, required_training_hours, attended_training_hours):
        """
        Preconditions: Valid ProductionWorker args; monthly_bonus is a positive float;
                       required_training_hours and attended_training_hours are positive ints
        Postconditions: TeamLeader object initialized with all attributes
        """
        super().__init__(name, employee_number, hire_date, shift, hourly_pay_rate)
        self._monthly_bonus = monthly_bonus
        self._required_training_hours = required_training_hours
        self._attended_training_hours = attended_training_hours

    # ---- Getters and Setters ----

    @property
    def monthly_bonus(self):
        return self._monthly_bonus

    @monthly_bonus.setter
    def monthly_bonus(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._monthly_bonus = value
        else:
            raise ValueError("Monthly bonus must be positive.")

    @property
    def required_training_hours(self):
        return self._required_training_hours

    @required_training_hours.setter
    def required_training_hours(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._required_training_hours = value
        else:
            raise ValueError("Required training hours must be positive.")

    @property
    def attended_training_hours(self):
        return self._attended_training_hours

    @attended_training_hours.setter
    def attended_training_hours(self, value):
        # Precondition: value must be positive
        if value > 0:
            self._attended_training_hours = value
        else:
            raise ValueError("Attended training hours must be positive.")

    # ---- Display ----

    def __str__(self):
        """Returns a user-friendly string representation."""
        return (f"{super().__str__()}\n"
                f"  Monthly Bonus: ${self._monthly_bonus:,.2f}\n"
                f"  Required Training Hours: {self._required_training_hours}\n"
                f"  Attended Training Hours: {self._attended_training_hours}")

    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return (f"TeamLeader({self._name!r}, {self._employee_number!r}, "
                f"{self._hire_date!r}, {self._shift!r}, {self._hourly_pay_rate!r}, "
                f"{self._monthly_bonus!r}, {self._required_training_hours!r}, "
                f"{self._attended_training_hours!r})")

    def print_team_leader(self):
        """
        Preconditions: None
        Postconditions: Displays production worker info plus team leader data
        """
        print(self.__str__())


# ---- Unit Tests ----
if __name__ == "__main__":
    print("=" * 50)
    print("TeamLeader Class - Unit Tests")
    print("=" * 50)

    tl1 = TeamLeader("Frank Miller", 4001, "03/15/2017", 1, 25.00,
                     500.00, 40, 35)
    print("\nTeam Leader 1:")
    tl1.print_team_leader()
