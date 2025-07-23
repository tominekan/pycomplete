"""
Test pycomplete/pycomplete.py
"""

from pycomplete.pycomplete import PyComplete
import pytest

# TEST: predict
def test_empty_pycomplete():
    """
    Tests that this works even when we pass in an empty string
    """

    p = PyComplete("")
    assert len(p.predict("lebron")) == 0


def test_singleton_pycomplete():
    """
    Tests that this works even when we pass in a string with only a single word
    """

    p = PyComplete("lebron")
    assert len(p.predict("lebron")) == 0


def test_predict_throws_error_num_less_one():
    """
    Tests that when we pass in num less than 1, 
    """

    with pytest.raises(ValueError):
        p = PyComplete("lebron james")
        p.predict("lebron", num=0)


def test_predict_works_properly_easy():
    """
    Tests that predict works in the normal use case (EASY)
    """

    p = PyComplete("lebron james is the greatest ")
    assert p.predict("l") == ["lebron", "james"]

def test_predict_works_properly_harder():
    """
    Tests that predict works in the normal use case (HARDER)
    """

    p = PyComplete("no one not two note three noted four no one no two no two no two")
    assert p.predict("n") == ["no", "two"]
    assert p.predict("no") == ["no", "two"]
    assert p.predict("not") == ["not", "two"]
    assert p.predict("note") == ["note", "three"]
    assert p.predict("noted") == ["noted", "four"]

# TEST: add_pair
def test_add_pair_influences_decisons():
    """
    Tests that add_pair influences
    """
    p = PyComplete("no one not two note three noted four no one")
    assert p.predict("n") == ["no", "one"]
    assert p.predict("no") == ["no", "one"]
    assert p.predict("not") == ["not", "two"]
    assert p.predict("note") == ["note", "three"]
    assert p.predict("noted") == ["noted", "four"]
    p.add_pair("no", "two")
    p.add_pair("no", "two")
    p.add_pair("no", "two")
    assert p.predict("n") == ["no", "two"]
    assert p.predict("no") == ["no", "two"]

def test_add_pair_nonexistent_value():
    """
    Tests that add_pair works properly for values that don't exist
    """

    p = PyComplete("no one not two note three noted four no one")
    assert p.predict("n") == ["no", "one"]
    assert p.predict("no") == ["no", "one"]
    assert p.predict("not") == ["not", "two"]
    assert p.predict("note") == ["note", "three"]
    assert p.predict("noted") == ["noted", "four"]
    p.add_pair("no", "ten")
    p.add_pair("no", "ten")
    p.add_pair("no", "ten")
    assert p.predict("n") == ["no", "ten"]
    assert p.predict("no") == ["no", "ten"]

def test_add_pair_nonexistent_key():
    """
    Tests that add_pair works properly for keys that don't exist
    """

    p = PyComplete("no one not two note three noted four no one")
    assert p.predict("n") == ["no", "one"]
    assert p.predict("no") == ["no", "one"]
    assert p.predict("not") == ["not", "two"]
    assert p.predict("note") == ["note", "three"]
    assert p.predict("noted") == ["noted", "four"]
    p.add_pair("n", "one")
    p.add_pair("n", "one")
    p.add_pair("n", "one")
    assert p.predict("n") == ["n", "one"]

def test_add_pair_nonexistent_key_value():
    """
    Tests that add_pair works properly for keys and values that don't exist
    """

    p = PyComplete("no one not two note three noted four no one")
    assert p.predict("n") == ["no", "one"]
    assert p.predict("no") == ["no", "one"]
    assert p.predict("not") == ["not", "two"]
    assert p.predict("note") == ["note", "three"]
    assert p.predict("noted") == ["noted", "four"]
    p.add_pair("n", "ten")
    p.add_pair("n", "ten")
    p.add_pair("n", "ten")
    assert p.predict("n") == ["n", "ten"]