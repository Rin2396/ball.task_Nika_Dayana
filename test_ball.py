""""""
import pytest
from typing import Tuple
from ball import gradus_get


test_znacheniya = (
    (5, 5, 5, 5, 360.79),
    (7, 7, 7, 7, 360.01),
    (4.5, 5, 6, 7.8, 360.03),
    (78, 60, 1.5, 0, 360.51),
)


@pytest.mark.parametrize('radius, time, acceleration, velocity, gradus', test_znacheniya)
def test_gradus(radius: float, time: float, acceleration: float, velocity: float, gradus: Tuple[float]):
    """"""
    assert gradus_get(radius, time, acceleration, velocity) == gradus


@pytest.mark.xfail(raises=Exception)
def test_exception():
    """"""
    assert gradus_get(0, -6, 5, 5)
