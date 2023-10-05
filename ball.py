"""Programm that is supposed to calculate degrees traveled by ball."""
from math import pi

BALL_DEGREES = 360


def gradus_get(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    """Section of code to find of the degree for ball displacement.

    Args:
        radius: float ball radius.
        time: float how much time has passed.
        acceleration: float how fast it moves.
        velocity: float velosity that was given.

    Returns:
        float: degree of dosplacement.

    Raises:
        ValueError: if first two arguments are incorrect.

    """
    if radius <= 0:
        raise ValueError(f'Incorrect radius entered: {radius}')
    elif time < 0:
        raise ValueError(f'Incorrect radius entered: {time}')
    dlina = 2 * pi * radius
    dist = velocity * time + (acceleration * time ** 2) / 2
    gradus = ((dist % dlina) / dlina) + BALL_DEGREES
    return round(gradus, 2)
