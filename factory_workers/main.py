"""
Factory Workers - Integration Test (main.py)
Demonstrates the Employee -> ProductionWorker -> TeamLeader hierarchy
and the Employee -> ShiftSupervisor hierarchy.
"""

from employee import Employee
from production_worker import ProductionWorker
from shift_supervisor import ShiftSupervisor
from team_leader import TeamLeader


def main():
    print("=" * 60)
    print("Factory Workers Class Hierarchy - Integration Test")
    print("=" * 60)

    # ---- Employee Tests ----
    print("\n--- Employee ---")
    emp = Employee("Alice Johnson", 1001, "03/15/2020")
    emp.print_employee()

    # ---- ProductionWorker Tests ----
    print("\n--- Production Worker 1 ---")
    pw1 = ProductionWorker("Carlos Diaz", 2001, "01/10/2021", 1, 18.50)
    pw1.print_production_worker()

    print("\n--- Production Worker 2 ---")
    pw2 = ProductionWorker("Diana Prince", 2002, "07/22/2022", 2, 22.75)
    pw2.print_production_worker()

    # ---- ShiftSupervisor Test ----
    print("\n--- Shift Supervisor ---")
    ss = ShiftSupervisor("Emily Carter", 3001, "05/01/2018", 65000.00, 5000.00)
    ss.print_shift_supervisor()

    # ---- TeamLeader Test ----
    print("\n--- Team Leader ---")
    tl = TeamLeader("Frank Miller", 4001, "03/15/2017", 1, 25.00,
                    500.00, 40, 35)
    tl.print_team_leader()


if __name__ == "__main__":
    main()
