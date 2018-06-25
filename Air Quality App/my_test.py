# import os

# from my_script import enlarge
#
# def test_enlarge():
#     result = enlarge(3)
#     assert result == 400

# test_enlarge()

from app import validate

def test_validate():
    print("hello")
    result = validate("2018-06-25")
    assert result == True

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    test_validate()
