import pytest

from tapyr_template.logic.utils import divide
from tests.helpers.logging_helpers import log_contain_message


def test_divide():
    # Given
    x = 2
    y = 2
    expected = 1.0
    # When
    result = divide(x, y)
    # Then
    assert result == expected


def test_divide_by_zero(loguru_sink):
    # Given
    x = 2
    y = 0
    # When
    with pytest.raises(ZeroDivisionError):
        divide(x, y)
    # Then
    assert log_contain_message(loguru_sink, "ZeroDivisionError: division by zero")
