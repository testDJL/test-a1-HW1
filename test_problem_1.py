from main import *

def test_myName():
    # Check if the result of myName() is a string
    assert isinstance(myName(), str), "myName() should return a string"