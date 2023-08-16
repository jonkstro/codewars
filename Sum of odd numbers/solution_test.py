import pytest
from solution import row_sum_odd_numbers

def test_row_sum_odd_numbers_1():
    assert row_sum_odd_numbers(1) == 1

def test_row_sum_odd_numbers_2():
    assert row_sum_odd_numbers(2) == 8

def test_row_sum_odd_numbers_13():
    assert row_sum_odd_numbers(13) == 2197

def test_row_sum_odd_numbers_19():
    assert row_sum_odd_numbers(19) == 6859

def test_row_sum_odd_numbers_41():
    assert row_sum_odd_numbers(41) == 68921
