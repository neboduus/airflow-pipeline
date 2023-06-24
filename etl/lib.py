import logging
from datetime import datetime
from io import StringIO
from typing import Union

import pandas as pd
from pandas._libs import NaTType

logger = logging.getLogger(__name__)


def read_data(data: str, sep: str = ',') -> pd.DataFrame:
    df = pd.read_csv(StringIO(data), sep=sep)
    return df.rename(columns=lambda x: x.strip())


def parse_birthdate(birthdate: str, date_format: str = "%Y-%m-%d") -> Union[datetime, NaTType]:
    try:
        return datetime.strptime(birthdate, date_format)
    except (Exception,):
        return pd.NaT


def convert_birthdate(employee_df: pd.DataFrame) -> pd.DataFrame:
    employee_df['ParsedBirthDate'] = employee_df['BirthDate'].apply(parse_birthdate)
    return employee_df


def clean_text(text: str) -> Union[str, NaTType]:
    replacements_dict = {
        '!': '',
        '@': '',
        '&': '',
        '$': '',
        '"': '',
        '(': '',
        ')': '',
        '.': '',
        '\n': '',
        ';': '',
        '#': '',
        '*': '',
        '_': '',
        "'": '',
        "^": '',
        "=": '',
        # ' ': ''
    }
    try:
        for key, value in replacements_dict.items():
            if key in text:
                text = text.replace(key, value)
        return text.strip()
    except (Exception,):
        return pd.NaT


def clean_names(employee_df: pd.DataFrame) -> pd.DataFrame:
    employee_df['FirstName'] = employee_df['FirstName'].apply(clean_text)
    employee_df['LastName'] = employee_df['LastName'].apply(clean_text)
    return employee_df


def merge_names(employee_df: pd.DataFrame) -> pd.DataFrame:
    employee_df['MergedNames'] = employee_df['FirstName'] + ' ' + employee_df['LastName']
    return employee_df


def calculate_age(employee_df: pd.DataFrame) -> pd.DataFrame:
    today = datetime(2023, 1, 1, 0, 0)
    employee_df['Age'] = employee_df['ParsedBirthDate'] - today
    return employee_df


def calculate_salary_bucket(employee_df: pd.DataFrame) -> pd.DataFrame:
    pass
