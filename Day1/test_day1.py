import question
import pytest

def math(x):
    return x//3 - 2

def test_math():
    assert question.math(100756) == 33583
    assert question.math(12) == 2
    assert question.math(14) == 2
    assert question.math(1969) == 654


def test_total_fuel_func():
    assert question.total_fuel_func([33583, 11192, 3728, 1240, 411, 135], math) == 25029
    