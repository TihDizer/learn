
ETALON_DATA = [
    {
        'id': 3,
        'first_name': 'Jim',
        'last_name': 'Halpert',
        'hire_date': '2005-04-21',
        'department': 'Sales'
    },
    {
        'id': 5,
        'first_name': 'Ryan',
        'last_name': 'Howard',
        'hire_date': '2005-06-01',
        'department': 'Sales'
    },
    {
        'id': 10,
        'first_name': 'Stanley',
        'last_name': 'Hudson',
        'hire_date': '2005-11-20',
        'department': 'Sales'
    },
    {
        'id': 22,
        'first_name': 'Phyllis',
        'last_name': 'Smith',
        'hire_date': '2005-10-10',
        'department': 'Sales'
    },
    {
        'id': 9,
        'first_name': 'Phyllis',
        'last_name': 'Vance',
        'hire_date': '2005-10-01',
        'department': 'Sales'
    }
]


def test_json_correct(json_input_data: dict) -> None:
    """Проверка корректности итогового json файла"""
    assert json_input_data == ETALON_DATA
