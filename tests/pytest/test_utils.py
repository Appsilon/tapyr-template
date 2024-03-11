from pyshiny_template.utils.utils import square


def test_square():
    # Given
    x = 2
    # When
    result = square(x)
    # Then
    assert result == 4
