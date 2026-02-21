"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_cases():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6          # Test for positive numbers
    assert max_subarray_sum([-1]) == -1                            # Test for single negative number
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23                              # Test for single positive number
    assert max_subarray_sum([]) == float('-inf')                  # Test for empty list
    assert max_subarray_sum([-2, -3, -1]) == -1                   # Test for all negative numbers
    assert max_subarray_sum([1]) == 1                             # Test for single positive number

if __name__ == "__main__":
    pytest.main()