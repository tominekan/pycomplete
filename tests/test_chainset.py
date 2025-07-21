"""
Test chainset.py
"""

from pycomplete.chainset import ChainSet
import pytest

# TEST: add
def test_add_exists():
    """
    Tests if adding values makes the key exist
    """
    c = ChainSet()
    c.add("lebron", "james")
    assert c.exists("lebron")
