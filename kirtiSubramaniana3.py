#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Inheritance
# Description: Employee, ProductionWorker, and ShiftSupervisor classes.
# Filename: kirtisubramaniana1.py
# Date: 8/1/2023
#################################################################
from decimal import Decimal, ROUND_HALF_UP


class Employee:
    """Employee Class - Keeps data attributes for name and employee ID."""
    MAX_NAME_LENGTH = 20
    EMPLOYEE_ID_LENGTH = 8

    def __init__(self, name, employee_id):
        """Constructor for Employee class."""
        self._name = self._validate_name(name)
        self._employee_id = self._validate_employee_id(employee_id)

    def _validate_name(self, name):
        """Validates the name, truncates if longer than the maximum length."""
        return name[:self.MAX_NAME_LENGTH]

    def _validate_employee_id(self, employee_id):
        """Validates the employee ID as an 8-digit number."""
        if len(str(employee_id)) != self.EMPLOYEE_ID_LENGTH:
            raise ValueError("Employee ID must be an 8-digit number.")
        return employee_id

    def get_name(self):
        """Accessor for employee's name."""
        return self._name

    def get_employee_id(self):
        """Accessor for employee's ID number."""
        return self._employee_id

    @staticmethod
    def _validate_hourly_pay_rate(hourly_pay_rate):
        if hourly_pay_rate < 0:
            raise ValueError("Hourly pay rate cannot be negative.")
        return hourly_pay_rate


class ProductionWorker(Employee):
    """ProductionWorker Class - Subclass of Employee, stores shift and pay rate."""
    DAY_SHIFT = 1
    NIGHT_SHIFT = 2

    def __init__(self, name, employee_id, shift_number, hourly_pay_rate):
        """Constructor for ProductionWorker class."""
        super().__init__(name, employee_id)
        self._shift_number = self._validate_shift_number(shift_number)
        self._hourly_pay_rate = self._validate_hourly_pay_rate(hourly_pay_rate)

    def _validate_shift_number(self, shift_number):
        """Validates the shift number (1 for day shift, 2 for night shift)."""
        if shift_number not in [self.DAY_SHIFT, self.NIGHT_SHIFT]:
            raise ValueError("Invalid shift number. Choose 1 for day shift or 2 for night shift.")
        return shift_number

    def get_shift_number(self):
        """Accessor for employee's shift number."""
        return self._shift_number

    def get_hourly_pay_rate(self):
        """Accessor for employee's hourly pay rate."""
        return self._hourly_pay_rate


class ShiftSupervisor(Employee):
    """ShiftSupervisor Class - Subclass of Employee, stores salary and bonus."""

    def __init__(self, name, employee_id, annual_salary, annual_production_bonus):
        """Constructor for ShiftSupervisor class."""
        super().__init__(name, employee_id)
        self._annual_salary = self._validate_annual_salary(annual_salary)
        self._annual_production_bonus = self._validate_annual_production_bonus(annual_production_bonus)

    def get_annual_salary(self):
        """Accessor for shift supervisor's annual salary."""
        return self._annual_salary

    def get_annual_production_bonus(self):
        """Accessor for shift supervisor's annual production bonus."""
        return self._annual_production_bonus

    @staticmethod
    def _validate_annual_production_bonus(annual_production_bonus):
        if annual_production_bonus < 0:
            raise ValueError("Annual production bonus cannot be negative.")
        return annual_production_bonus

    @staticmethod
    def _validate_annual_salary(annual_salary):
        if annual_salary < 0:
            raise ValueError("Annual salary cannot be negative.")
        return annual_salary


def format_currency(amount):
    """Formats the given amount as currency."""
    return "${:,.2f}".format(amount.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
