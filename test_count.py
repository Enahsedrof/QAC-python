import pytest
import count

def test_count_zeroes():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a", "a", "a"], "a") == 3

test_count_zeroes()
test_count_string()