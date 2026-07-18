from pathlib import Path

import pytest
from pandas.core.generic import FilePath


@pytest.fixture
def csv_file() -> FilePath:
    """Фикстура для доступа к csv файлу для проверки"""
    return Path('.') / 'pgadmin.csv'
