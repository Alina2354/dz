import pytest

def test_multiply():
    assert 3 * 4 == 12

def test_multiply_int_str():
    assert 3 * 'asd' == 'asdasdasd'

def test_multiply_strings():
    with pytest.raises(TypeError):
         'asd' * 'asdf'




