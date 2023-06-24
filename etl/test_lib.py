import json
import logging
import os
from pathlib import Path

from etl.lib import read_data, convert_birthdate

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


def test_birthdate_conversion():
    employee_df = convert_birthdate(read_data(get_employee_data()))
    expected_test_resource = "expected_birthdate_column_after_conversion.json"
    expected_birthdate_col_json = get_test_resource(expected_test_resource)
    parsed_birthdate_col_json = json.loads(employee_df["ParsedBirthDate"].to_json())
    assert expected_birthdate_col_json == parsed_birthdate_col_json
