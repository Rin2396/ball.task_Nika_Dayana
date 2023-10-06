"""Test to check the functionality of the function."""
import pytest

from ball import get_gradus

test_values = (
    (5, 5, 5, 5, 360.79),
    (7, 7, 7, 7, 360.01),
    (4.5, 5, 6, 7.8, 360.03),
    (78, 60, 1.5, 0, 360.51),
    (1, 2, 3, 4, 360.23),
    (3, 1, 10, 22, 360.43),
    (10, 9, 3, 4, 360.51),
    (100, 100, 100, 100, 360.69),
    (91, 72, 53, 34, 360.55)
)


@pytest.mark.parametrize('radius, time, acceleration, velocity, expected', test_values)
def test_gradus(radius: float, time: float, acceleration: float, velocity: float, expected: float):
    """Section of code to find of the degree for ball displacement.

    Args:
        radius: float ball radius.
        time: float how much time has passed.
        acceleration: float how fast it moves.
        velocity: float velosity that was given.
        expected: float degree that is supposed to be returned.

    """
    assert get_gradus(radius, time, acceleration, velocity) == expected


@pytest.mark.xfail(raises=Exception)
def test_exception():
    """Exception test that has no args or returns."""
    assert get_gradus(0, -6, 5, 5)
