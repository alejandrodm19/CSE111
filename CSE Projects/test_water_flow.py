from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest
import math


def test_water_column_height():
    # Test case 1: Tower height = 0, Tank wall height = 0
    result = water_column_height(0, 0)
    assert result == 0

    # Test case 2: Tower height = 0, Tank wall height = 10
    result = water_column_height(0, 10)
    assert result == 7.5

    # Test case 3: Tower height = 25, Tank wall height = 0
    result = water_column_height(25, 0)
    assert result == 25

    # Test case 4: Tower height = 48.3, Tank wall height = 12.8
    result = water_column_height(48.3, 12.8)
    assert round(result, 1) == 57.9

def test_pressure_gain_from_water_height():
    # Test case 1: Height = 0
    result = pressure_gain_from_water_height(0)
    assert result == 0

    # Test case 2: Height = 30.2
    result = pressure_gain_from_water_height(30.2)
    assert abs(result - 295.628) < 0.001

    # Test case 3: Height = 50
    result = pressure_gain_from_water_height(50)
    assert abs(result - 489.450) < 0.001
    

def test_pressure_loss_from_pipe():
    # Test case 1
    result = pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75)
    assert abs(result - 0) < 0.001

    # Test case 2
    result = pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert abs(result - 0) < 0.001

    # Test case 3
    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert abs(result - 0) < 0.001

    # Test case 4
    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert abs(result - (-113.008)) < 0.001

    # Test case 5
    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert abs(result - (-100.462)) < 0.001

    # Test case 6
    result = pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert abs(result - (-61.576)) < 0.001

    # Test case 7
    result = pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert abs(result - (-110.884)) < 0.001
    

def test_pressure_loss_from_fittings():
    # Test case 1
    result = pressure_loss_from_fittings(0, 3)
    assert abs(result - 0) < 0.001

    # Test case 2
    result = pressure_loss_from_fittings(1.65, 0)
    assert abs(result - 0) < 0.001

    # Test case 3
    result = pressure_loss_from_fittings(1.65, 2)
    assert abs(result - (-0.109)) < 0.001

    # Test case 4
    result = pressure_loss_from_fittings(1.75, 2)
    assert abs(result - (-0.122)) < 0.001

    # Test case 5
    result = pressure_loss_from_fittings(1.75, 5)
    assert abs(result - (-0.306)) < 0.001
    
def test_reynolds_number():
    # Test case 1
    result = reynolds_number(0.048692, 0)
    assert abs(result - 0) < 1

    # Test case 2
    result = reynolds_number(0.048692, 1.65)
    assert abs(result - 80069) < 1

    # Test case 3
    result = reynolds_number(0.048692, 1.75)
    assert abs(result - 84922) < 1

    # Test case 4
    result = reynolds_number(0.28687, 1.65)
    assert abs(result - 471729) < 1

    # Test case 5
    result = reynolds_number(0.28687, 1.75)
    assert abs(result - 500318) < 1


def test_pressure_loss_from_pipe_reduction():
    # Test case 1
    larger_diameter = 0.28687
    fluid_velocity = 0
    reynolds_number = 1
    smaller_diameter = 0.048692
    expected_pressure_loss = 0
    tolerance = 0.001
    result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
    assert math.isclose(result, expected_pressure_loss, rel_tol=tolerance), f"Test case 1 failed. Expected: {expected_pressure_loss}, Actual: {result}"

    # Test case 2
    larger_diameter = 0.28687
    fluid_velocity = 1.65
    reynolds_number = 471729
    smaller_diameter = 0.048692
    expected_pressure_loss = -163.744
    tolerance = 0.001
    result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
    assert math.isclose(result, expected_pressure_loss, rel_tol=tolerance), f"Test case 2 failed. Expected: {expected_pressure_loss}, Actual: {result}"

    # Test case 3
    larger_diameter = 0.28687
    fluid_velocity = 1.75
    reynolds_number = 500318
    smaller_diameter = 0.048692
    expected_pressure_loss = -184.182
    tolerance = 0.001
    result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
    assert math.isclose(result, expected_pressure_loss, rel_tol=tolerance), f"Test case 3 failed. Expected: {expected_pressure_loss}, Actual: {result}"
    
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
