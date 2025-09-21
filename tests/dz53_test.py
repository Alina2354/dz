import pytest
from dz53 import reverse_words

@pytest.fixture
def simple_string():
    return "The quick brown fox"

@pytest.fixture
def empty_string():
    return ""

@pytest.fixture
def single_word():
    return "Hello"

def test_reverse_simple(simple_string):
    assert reverse_words(simple_string) == "fox brown quick The"

def test_reverse_empty(empty_string):
    assert reverse_words(empty_string) == ""

def test_reverse_single(single_word):
    assert reverse_words(single_word) == "Hello"



