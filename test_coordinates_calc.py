#testing coordinate function

import pytest

@pytest.mark.parametrize("input1, input2, input3, expected",[
    ((1,2),(2,1), 3, 0),
    ((3,4),(5,6), 8, 9)])
def test_y(input1, input2, input3, expected):
    from coordinates_calc import input_val
    answer = input_val(input1, input2, input3)
    assert answer == expected

@pytest.mark.parametrize("input1, input2, input3,input4, expected",[
    (1,2,2,1, -1),
    (3,4, 5,6, 1)])
def test_slopeee(input1, input2, input3,input4, expected):
    from coordinates_calc import slope_calc
    answer = slope_calc(input1, input2, input3, input4)
    assert answer == expected

@pytest.mark.parametrize("input1, input2, input3,input4, expected",[
    (1,2,-1, 3, 0),
    (3,4,1,8,9)])
def test_calculation(input1, input2, input3,input4, expected):
    from coordinates_calc import y_val
    answer = y_val(input1, input2, input3,input4)
    assert answer == expected
