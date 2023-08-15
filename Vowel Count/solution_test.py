import pytest
from solution import get_count

@pytest.mark.it("Should count all vowels")
def test_all_vowels():
    assert get_count("aeiou") == 5

@pytest.mark.it("Should not count \"y\"")
def test_only_y():
    assert get_count("y") == 0

@pytest.mark.it("Should return 0 when no vowels")
def test_no_vowels():
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0

@pytest.mark.it("Should return 0 for empty string")
def test_empty_string():
    assert get_count("") == 0

@pytest.mark.it("Should return 5 for \"abracadabra\"")
def test_abracadabra():
    assert get_count("abracadabra") == 5
