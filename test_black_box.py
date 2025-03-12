import pytest
from main import check_password


def test__boundary_values_password():
    assert check_password(36, True, False) == "medium"
    assert check_password(36, True, True) == "strong"
    assert check_password(36, False, True) == "medium"
    assert check_password(7, True, True) == "invalid"
    assert check_password(8, True, True) == "weak"
    assert check_password(9, True, True) == "weak"
    assert check_password(15, True, True) == "weak"
    assert check_password(16, True, True) == "strong"
    assert check_password(17, True, True) == "strong"
    assert check_password(63, True, True) == "strong"
    assert check_password(64, True, True) == "strong"
    assert check_password(65, True, True) == "invalid"


def test_equivalence_partitioning_password():
    assert check_password(5, True, False) == "invalid"
    assert check_password(120, False, False) == "invalid"
    assert check_password(12, True, True) == "weak"
    assert check_password(12, True, False) == "weak"
    assert check_password(12, False, True) == "weak"
    assert check_password(12, False, False) == "weak"
    assert check_password(25, True, True) == "strong"
    assert check_password(25, True, False) == "medium"
    assert check_password(25, False, True) == "medium"
    assert check_password(25, False, False) == "weak"
