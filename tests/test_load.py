import pytest
from src.extract import extract_weather_data
from src.load import create_database_engine, load_data_into_database_table, read_existing_table
from dotenv import load_dotenv
import os

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
    assert engine
    connection = engine.connect()
    print("Successfully connected to the database!")
    connection.close()
