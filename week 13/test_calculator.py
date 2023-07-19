from pytest import approx
import pytest
from allcalculator import add, multiply, subtract, divide, calculate_tax  

def test_add():
    assert add.add(5, 3) == 8

def test_subtract():
    assert subtract.subtract(5, 3) == 2

def test_multiply():
    assert multiply.multiply(5, 3) == 15

def test_divide():
    assert divide.divide(9, 3) == 3
    assert divide.divide(5, 0) == "Error: Division by zero is not allowed."

def test_calculate_tax():
    assert calculate_tax.calculate_tax(100, 10) == 10
