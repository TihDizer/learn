import pandas as pd
from pandas.core.generic import FilePath
from pandas.testing import assert_frame_equal


ETALON_DATA = {
    'flight_no': [
        'PG0639', 'PG0646', 'PG0131', 'PG0266', 'PG0464', 'PG0274', 'PG0594',
        'PG0631', 'PG0685', 'PG0039', 'PG0102', 'PG0499', 'PG0692', 'PG0175',
        'PG0276', 'PG0174', 'PG0056', 'PG0111', 'PG0278', 'PG0511'
    ],
    'departure_airport': [
        'DME', 'RTW', 'URS', 'HMA', 'RTW', 'CEK', 'KVX', 'PES', 'LED',
        'KZN', 'SVX', 'IKT', 'KVX', 'VOG', 'HTA', 'SVO', 'TBW', 'TJM',
        'OVB', 'NAL'
    ],
    'arrival_airport': [
        'NYM', 'DME', 'KUF', 'NUX', 'ULY', 'DME', 'DME', 'TJM', 'OVS',
        'KVX', 'KGP', 'KZN', 'HMA', 'SVO', 'NUX', 'VOG', 'DME', 'UCT',
        'SVO', 'GOJ'
    ],
    'departure_airport_name': [
        'Домодедово', 'Саратов-Центральный', 'Курск-Восточный',
        'Ханты-Мансийск', 'Саратов-Центральный', 'Челябинск',
        'Победилово', 'Бесовец', 'Пулково', 'Казань', 'Кольцово',
        'Иркутск', 'Победилово', 'Гумрак', 'Чита', 'Шереметьево',
        'Донское', 'Рощино', 'Толмачёво', 'Нальчик'
    ],
    'actual_arrival': [
        '2017-08-15 15:00:00+00:00', '2017-08-15 14:58:00+00:00',
        '2017-08-15 14:58:00+00:00', '2017-08-15 14:57:00+00:00',
        '2017-08-15 14:56:00+00:00', '2017-08-15 14:55:00+00:00',
        '2017-08-15 14:53:00+00:00', '2017-08-15 14:53:00+00:00',
        '2017-08-15 14:53:00+00:00', '2017-08-15 14:53:00+00:00',
        '2017-08-15 14:53:00+00:00', '2017-08-15 14:53:00+00:00',
        '2017-08-15 14:52:00+00:00', '2017-08-15 14:51:00+00:00',
        '2017-08-15 14:46:00+00:00', '2017-08-15 14:46:00+00:00',
        '2017-08-15 14:46:00+00:00', '2017-08-15 14:43:00+00:00',
        '2017-08-15 14:43:00+00:00', '2017-08-15 14:41:00+00:00'
    ]
}


def execute_sql_query() -> pd.DataFrame:
    """Возвращает эталонные данные в виде DataFrame"""
    df = pd.DataFrame(ETALON_DATA)
    df.index = range(len(df))
    df.sort_index()
    return df


def test_csv_structure(csv_file: FilePath):
    """Проверяет структуру CSV-файла (столбцы и типы данных)"""
    df = pd.read_csv(csv_file)
    assert list(df.columns) == [
        'flight_no',
        'departure_airport',
        'arrival_airport',
        'departure_airport_name',
        'actual_arrival'
    ]
    assert pd.api.types.is_string_dtype(df['flight_no'])
    assert pd.api.types.is_string_dtype(df['departure_airport'])
    assert pd.api.types.is_string_dtype(df['arrival_airport'])
    assert pd.api.types.is_string_dtype(df['departure_airport_name'])


def test_sort_order(csv_file: FilePath):
    """Проверяет сортировку по actual_arrival (DESC)"""
    df = pd.read_csv(csv_file, parse_dates=['actual_arrival'])
    assert df['actual_arrival'].is_monotonic_decreasing, "Данные не отсортированы по убыванию даты"


def test_data_correctness(csv_file: FilePath):
    """Сравнивает данные CSV с результатом SQL-запроса"""
    df_csv = pd.read_csv(csv_file)
    df_db = execute_sql_query()
    assert_frame_equal(
        df_csv.reset_index(drop=True),
        df_db.reset_index(drop=True),
        check_dtype=False
    )
