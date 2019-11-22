"""
Unit tests from preprocessing functions
"""

# Docstring are superfluous for test functions
# pylint: disable=missing-docstring

from math import isclose
import numpy as np
from mlcore.preprocessing import train_test_split, scale_min_max, scale_standard


def test_train_test_split() -> None:
    # Generate a random (3,3) tensor
    x = np.random.rand(30, 3)

    x_train, x_test = train_test_split(x, test_ratio=.33)
    assert x_train.shape == (20, 3)
    assert x_test.shape == (10, 3)

    # Default ratio is 0.25
    x_train, x_test = train_test_split(x)
    assert x_train.shape == (22, 3)
    assert x_test.shape == (8, 3)


def test_scale_min_max() -> None:
    # Generate a random (3,3) tensor with values between 1 and 10
    x = np.random.randint(1, 10, (3, 3))

    x_scaled = scale_min_max(x)
    assert x_scaled.min() == 0
    assert x_scaled.max() == 1


def test_scale_standard() -> None:
    # Generate a random(3, 3) tensor with values between 1 and 10
    x = np.random.randint(1, 10, (3, 3))

    x_scaled = scale_standard(x)

    mean_scaled = x_scaled.mean()
    std_scaled = x_scaled.std()
    # https://stackoverflow.com/a/35325039
    assert isclose(mean_scaled, 0, abs_tol=1.0e-9)
    assert isclose(std_scaled, 1)
