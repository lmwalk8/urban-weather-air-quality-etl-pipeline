import pytest
from src.extract import extract_weather_data

EXPECTED_COLUMNS = 46
EXPECTED_ROWS = 1000

@pytest.fixture()
def extract_data():
    df = extract_weather_data()
    return df

@pytest.mark.extraction
def test_extract_data_shape(extract_data):
    df = extract_data
    assert len(df.columns) == EXPECTED_COLUMNS, "Actual number of columns does not match expected."
    assert len(df) == EXPECTED_ROWS, "Actual number of rows does not match expected."

@pytest.mark.extraction
def test_extract_data_column_values(extract_data):
    df = extract_data
    expected_column_names = ['datetime', 'datetimeEpoch', 'tempmax', 'tempmin', 'temp', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity', 'precip', 'precipprob', 'precipcover', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed', 'winddir', 'pressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'sunrise', 'sunriseEpoch', 'sunset', 'sunsetEpoch', 'moonphase', 'conditions', 'description', 'icon', 'stations', 'source', 'City', 'Temp_Range', 'Heat_Index', 'Severity_Score', 'Condition_Code', 'Month', 'Season', 'Day_of_Week', 'Is_Weekend', 'Health_Risk_Score']
    assert df.columns.to_list() == expected_column_names

@pytest.mark.extraction
def test_extract_data_city_names(extract_data):
    df = extract_data
    expected_city_names = ['Phoenix', 'San Jose', 'San Antonio', 'Los Angeles', 'San Diego', 'New York City', 'Chicago', 'Philadelphia', 'Dallas', 'Houston']
    assert df["City"].unique().tolist() == expected_city_names
