#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Inheritance
# Description:Test driver for ProductionWorker and ShiftSupervisor.
# Filename: kirtisubramaniana1.py
# Date: 8/1/2023
#################################################################
from decimal import Decimal
from kirtiSubramaniana3 import ProductionWorker, ShiftSupervisor, format_currency


def test_program():
    # Test ProductionWorker
    print("Demo Production Worker")
    name = input("Enter the name: ")
    employee_id = input("Enter the ID number: ")
    shift_number = int(input("Enter the shift number (1 for day shift, 2 for night shift): "))
    hourly_pay_rate = Decimal(input("Enter the hourly pay rate: "))
    production_worker = ProductionWorker(name, employee_id, shift_number, hourly_pay_rate)

    print("\nProduction worker information:")
    print("Name:", production_worker.get_name())
    print("ID number:", production_worker.get_employee_id())
    print("Shift number:", production_worker.get_shift_number())
    print("Hourly pay rate:", format_currency(production_worker.get_hourly_pay_rate()))

    # Test ShiftSupervisor
    print("\nDemo Shift Supervisor")
    name = input("Enter the name: ")
    employee_id = input("Enter the ID number: ")
    annual_salary = Decimal(input("Enter the annual salary: "))
    annual_production_bonus = Decimal(input("Enter the annual production bonus: "))
    shift_supervisor = ShiftSupervisor(name, employee_id, annual_salary, annual_production_bonus)

    print("\nShift supervisor information:")
    print("Name:", shift_supervisor.get_name())
    print("ID number:", shift_supervisor.get_employee_id())
    print("Annual Salary:", format_currency(shift_supervisor.get_annual_salary()))
    print("Annual Production Bonus:", format_currency(shift_supervisor.get_annual_production_bonus()))


if __name__ == "__main__":
    test_program()


# Test Output
"""
/Users/kirtisubramanian/PycharmProjects/CS_3B_Summer_23/venv/bin/python /Users/kirtisubramanian/PycharmProjects/CS_3B_Summer_23/kirtiSubramaniantest3.py 
Demo Production Worker
Enter the name: Kirti
Enter the ID number: 12345678
Enter the shift number (1 for day shift, 2 for night shift): 1
Enter the hourly pay rate: 51

Production worker information:
Name: Kirti
ID number: 12345678
Shift number: 1
Hourly pay rate: $51.00

Demo Shift Supervisor
Enter the name: Itrik
Enter the ID number: 87654321
Enter the annual salary: 149000
Enter the annual production bonus: 23000

Shift supervisor information:
Name: Itrik
ID number: 87654321
Annual Salary: $149,000.00
Annual Production Bonus: $23,000.00

Process finished with exit code 0
"""