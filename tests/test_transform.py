import pytest
from src.extract import extract_weather_data
from src.transform import transform_data

EXPECTED_WEATHER_COLUMNS = 43
EXPECTED_AIR_QUALITY_COLUMNS = 9

@pytest.fixture()
def transformed_data():
    df = extract_weather_data()
    weather_df, air_quality_df = transform_data(df)
    return weather_df, air_quality_df

@pytest.mark.transformation
def test_transform_data_shape(transformed_data):
    weather_df, air_quality_df = transformed_data
    assert len(weather_df.columns) == EXPECTED_WEATHER_COLUMNS, "Actual number of columns does not match expected."
    assert len(air_quality_df.columns) == EXPECTED_AIR_QUALITY_COLUMNS, "Actual number of columns does not match expected."

@pytest.mark.transformation
def test_transform_dataframes_no_nulls_or_duplicates(transformed_data):
    weather_df, air_quality_df = transformed_data
    assert weather_df.isnull().sum().sum() == 0, "Weather DataFrame contains null values."
    assert air_quality_df.isnull().sum().sum() == 0, "Air quality DataFrame contains null values."
    assert weather_df.duplicated().sum() == 0, "Weather DataFrame contains duplicates."
    assert air_quality_df.duplicated().sum() == 0, "Air quality DataFrame contains duplicates."
