import pytest
from main import check_password


def test_control_flow_password():
    assert check_password(5, True, False) == "invalid"
    assert check_password(26, True, True) == "strong"
    assert check_password(26, False, True) == "medium"
    assert check_password(12, False, True) == "weak"

