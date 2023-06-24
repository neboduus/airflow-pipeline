import logging
import os
from pathlib import Path

from etl.lib import read_data

logger = logging.getLogger(__name__)
current_path = Path(os.path.dirname(os.path.realpath(__file__)))


def test_read_data():
    employee_data = get_employee_data()
    employee_df = read_data(employee_data)
    assert not employee_df.empty


def get_employee_data():
    with open(f"{current_path}/data/employee_data.csv") as csv_file:
        employee_data = ''.join(csv_file.readlines())
    return employee_data
