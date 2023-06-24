import logging
from io import StringIO

import pandas as pd

logger = logging.getLogger(__name__)


def read_data(data: str, sep: str = ','):
    return pd.read_csv(StringIO(data), sep=sep)
