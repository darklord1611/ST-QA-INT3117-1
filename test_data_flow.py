import pytest
from main import check_password


def test_data_flow_password():
    assert check_password(5, True, False) == "invalid"
    assert check_password(25, True, True) == "strong"
    assert check_password(12, False, False) == "weak"
    assert check_password(29, False, True) == "medium"


    assert check_password(58, False, False) == "weak"
    assert check_password(66, True, False) == "invalid"
    assert check_password(36, True, True) == "strong"
    assert check_password(25, False, True) == "medium"
