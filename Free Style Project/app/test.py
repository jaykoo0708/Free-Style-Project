# from freestyle-project.expense-tracker import
import sys
import os
import json
from pprint import pprint

# with open('test.json') as f:
#     data = json.load(f)


sys.path.append(os.path.join('..', 'app')) #  name of folder that contain expense tracker py file

from app import validate

# def parse_response(response_text):
#     assert True == validate("2018-06-23")

def test_validate(): # only validating the date
    result = validate('2018-06-24')
    assert result == true


    #
    # try:
    #     datetime.datetime.strptime(date_text, '%Y-%m-%d')
    #     return True
    # except ValueError:
    #     raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    #     return False
