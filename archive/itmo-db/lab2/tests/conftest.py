import json
import pytest


@pytest.fixture
def json_input_data() -> dict:
    """Фикстура для доступа к json файлу для проверки"""
    with open('./employees_result.json') as f:
        return json.loads(f.read())
