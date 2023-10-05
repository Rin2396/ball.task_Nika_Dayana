"""Test to check the functionality of the function."""
import pytest

from ball import gradus_get

test_znacheniya = (
    (5, 5, 5, 5, 360.79),
    (7, 7, 7, 7, 360.01),
    (4.5, 5, 6, 7.8, 360.03),
    (78, 60, 1.5, 0, 360.51),
)


@pytest.mark.parametrize('radius, time, acceleration, velocity, expected', test_znacheniya)
def test_gradus(radius: float, time: float, acceleration: float, velocity: float, expected: float):
    """Section of code to find of the degree for ball displacement.

    Args:
        radius: float ball radius.
        time: float how much time has passed.
        acceleration: float how fast it moves.
        velocity: float velosity that was given.
        expected: float degree that is supposed to be returned.

    """
    assert gradus_get(radius, time, acceleration, velocity) == expected


@pytest.mark.xfail(raises=Exception)
def test_exception():
    """Exception test that has no args or returns."""
    assert gradus_get(0, -6, 5, 5)
