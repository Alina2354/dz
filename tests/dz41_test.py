import pytest
from dz41 import is_prime

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (-2, False),
    ('asd', pytest.raises(TypeError))
])
def test_is_prime(n, expected):
    if isinstance(expected, type(pytest.raises(TypeError))):
        with expected:
            is_prime(n)
    else:
        assert is_prime(n) == expected
