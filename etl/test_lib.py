import json
import logging
import os
import datetime
from pathlib import Path

import pandas as pd

from etl.lib import read_data, convert_birthdate, parse_birthdate, clean_text

logger = logging.getLogger(__name__)
current_path = Path(os.path.dirname(os.path.realpath(__file__)))


def get_test_resource(filename: str) -> dict:
    with open(current_path / 'test_resources' / filename) as file:
        return json.load(file)


def test_read_data():
    employee_data = get_employee_data()
    employee_df = read_data(employee_data)
    assert not employee_df.empty


def get_employee_data():
    with open(f"{current_path}/data/employee_data.csv") as csv_file:
        employee_data = ''.join(csv_file.readlines())
    return employee_data


def test_parse_birthdate():
    good_birthdate = "1990-08-07"
    bad_birthdate = "xxx-08-07"
    parsed_good_birthdate = parse_birthdate(good_birthdate)
    parsed_bad_birthdate = parse_birthdate(bad_birthdate)
    assert parsed_good_birthdate == datetime.datetime(1990, 8, 7, 0, 0)
    assert pd.isnull(parsed_bad_birthdate)


def test_birthdate_conversion():
    employee_df = convert_birthdate(read_data(get_employee_data()))
    expected_test_resource = "expected_birthdate_column_after_conversion.json"
    expected_birthdate_col_json = get_test_resource(expected_test_resource)
    parsed_birthdate_col_json = json.loads(employee_df["ParsedBirthDate"].to_json())
    assert expected_birthdate_col_json == parsed_birthdate_col_json


def test_clean_text():
    texts_test_cases = [
        ("D&Bry", "DBry"),
        ("Elena'00", "Elena00"),
        ('"J"ack "', "Jack"),
        ('Gabriel$   Lakey "', "Gabriel   Lakey")
    ]
    for input_text, expected_output in texts_test_cases:
        output = clean_text(input_text)
        assert output == expected_output
