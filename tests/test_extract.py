import pytest
from src.extract import extract_weather_data

EXPECTED_COLUMNS = 45
EXPECTED_ROWS = 1000

@pytest.fixture()
def extract_data():
    df = extract_weather_data()
    return df

@pytest.mark.extraction
def test_extract_data_shape(extract_data):
    df = extract_data
    assert df, "Data not extracted correctly from CSV file."
    assert len(df.columns) == EXPECTED_COLUMNS, "Actual number of columns does not match expected."
    assert len(df) == EXPECTED_ROWS, "Actual number of rows does not match expected."

@pytest.mark.extraction
def test_extract_data_column_values(extract_data):
    df = extract_data
    expected_column_names = ["temp", "score", "percipitation", "snow", "city_name"]
    assert df.columns.to_list() == expected_column_names

@pytest.mark.extraction
def test_extract_data_city_names(extract_data):
    df = extract_data
    expected_city_names = ["Philadelphia", "New York City", "Boston", "Chicago", "Phoenix", "Los Angeles"]
    assert df["city_name"].unique().to_list() == expected_city_names
