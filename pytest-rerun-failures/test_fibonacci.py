from fibonacci import fibonacci
from random import randint
import pytest

def test_fibonacci():
    assert fibonacci(8) == 21

def test_fibonacci_flaky():
    assert fibonacci(randint(7, 10)) == randint(20, 22)

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_fibonacci_flaky_2():
    assert fibonacci(randint(7, 10)) == randint(20, 22)
