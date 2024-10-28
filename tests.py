import pytest

from classes.squares import calculate_squares
from classes.coins import calculate_result

def test_squares():
    squares = calculate_squares()
    assert squares[0] == 100000
    assert squares[1] != 100_000
    squares = calculate_squares(-100)
    assert squares[0] < 0

def test_coins():
    array1 = [1, 2, 3, 4]
    array2 = [2, 4]
    result = calculate_result(array1, array2)
    assert result == [2, 4]
    array2 = [1, 3]
    result = calculate_result(array1, array2)
    assert result == []
    arrayS = ["test", 2]
    result = calculate_result(array1, array2)
    assert result == []



