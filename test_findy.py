import pytest

@pytest.mark.parametrize("x1, y1, x2, y2, tuple1, tuple2", [
    (1, 2, 3, 4, (1, 2), (3, 4))])
def test_tuple_time(x1, y1, x2, y2, tuple1, tuple2):
    from findy import tuple_time
    answer1, answer2 = tuple_time(x1, y1, x2, y2)
    print(answer1, answer2)
    assert answer1 == tuple1
    assert answer2 == tuple2

@pytest.mark.parametrize("x1, y1, x2, y2, m", [
    (1, 2, 3, 4, 1)])
def test_slopeing(x1, y1, x2, y2, m):
    from findy import slope
    mval = slope(x1, y1, x2, y2)
    print(m)
    assert mval == m

@pytest.mark.parametrize("m, xval, y1, x1, yout", [
    (2, 3, 3, 2, 5)])
def test_y_val(m, xval, y1, x1, yout):
    from findy import y_val
    yval = y_val(m, xval, y1, x1)
    print(yval)
    assert yval == yout
