import pytest
from solution import to_camel_case

def test_to_camel_case_empty_string():
    assert to_camel_case("") == ""

def test_to_camel_case_underscore():
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"

def test_to_camel_case_hyphen():
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"

def test_to_camel_case_multiple_hyphens():
    assert to_camel_case("A-B-C") == "ABC"
