import pytest
from src.extract import extract_weather_data
from src.load import create_database_engine, load_data_into_database_table, read_existing_table
from dotenv import load_dotenv
import os
import pandas as pd
import logging

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("Database URL is not set in the .env file")

@pytest.fixture()
def start_database_engine():
    engine = create_database_engine(DATABASE_URL)
    return engine

@pytest.mark.loading
def test_db_connection(start_database_engine):
    engine = start_database_engine
    assert engine, "Database engine is not created."
    connection = engine.connect()
    logging.info("Successfully connected to the database!")
    connection.close()

@pytest.mark.loading
def test_load_data_into_db_table_success(start_database_engine):
    engine = start_database_engine
    df = extract_weather_data()
    load_data_into_database_table(df, "weather_data", engine)
    logging.info("Data loaded into the database table successfully!")
    result = read_existing_table("weather_data", engine)
    assert result is not None, "Data is not fetched from the database table."
    logging.info("Data fetched from the database table successfully!")
    pd.testing.assert_frame_equal(df, result)
