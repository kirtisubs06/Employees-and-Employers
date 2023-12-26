# Python Inheritance Example: Employee Management System

## Course Information
- **Course**: CS 3B Intermediate Software Design in Python
- **Author**: Kirti Subramanian
- **Date**: 8/1/2023
- **Topic**: Inheritance
- **Filename**: kirtisubramaniana1.py

## Description
This Python script demonstrates the concept of inheritance in object-oriented programming. It defines a base class `Employee` and two subclasses `ProductionWorker` and `ShiftSupervisor`. The script showcases how to effectively use inheritance to create a simple yet scalable employee management system.

## Features

**Employee Class:**
- Base class with common attributes like name and employee ID.
- Methods for name and employee ID validation.
- Accessor methods for name and employee ID.

**ProductionWorker Class:**
- Inherits from `Employee`.
- Additional attributes for shift number and hourly pay rate.
- Methods for validating shift number and hourly pay rate.
- Accessor methods for shift number and hourly pay rate.

**ShiftSupervisor Class:**
- Inherits from `Employee`.
- Additional attributes for annual salary and annual production bonus.
- Methods for validating annual salary and annual production bonus.
- Accessor methods for annual salary and annual production bonus.

**Currency Formatting:**
- A utility function `format_currency` to format numeric values as currency.

## Installation

No additional installation required, as the script uses standard Python libraries.

## Usage

To use the script, simply import the classes and create instances of `ProductionWorker` or `ShiftSupervisor`:

```python
from kirtisubramaniana1 import ProductionWorker, ShiftSupervisor

# Example usage
worker = ProductionWorker("John Doe", 12345678, ProductionWorker.DAY_SHIFT, 15.0)
supervisor = ShiftSupervisor("Jane Doe", 87654321, 55000, 5000)

# Accessing attributes
print(worker.get_hourly_pay_rate())
print(supervisor.get_annual_salary())
