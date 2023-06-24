import logging
from datetime import datetime
from io import StringIO
from typing import Union

import pandas as pd
from pandas._libs import NaTType

logger = logging.getLogger(__name__)


def read_data(data: str, sep: str = ',') -> pd.DataFrame:
    return pd.read_csv(StringIO(data), sep=sep)


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
        # ' ': ''
    }
    try:
        for key, value in replacements_dict.items():
            if key in text:
                text = text.replace(key, value)
        return text.strip()
    except (Exception,):
        return pd.NaT
