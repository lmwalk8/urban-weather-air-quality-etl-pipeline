from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import logging

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("Database URL is not set in the .env file")

def create_database_engine():
    """
    Creates a PostgreSQL database engine based on the Database URL

    Returns:
        db (database engine): The PostgreSQL database engine.
    """
    try:
        db = create_engine(DATABASE_URL)
        return db
    except Exception as e:
        logging.error(f"Error creating database engine: {e}")

def load_data_into_database(df, table_name, db):
    """
    Loads data into table in PostgreSQL database.

    Parameters:
        df (pd.DataFrame): The raw weather data.
        table_name: Name of table the data will be loaded into.
        db: The database engine where the table will be.
    """
    # engine = create_database_engine()

    try:
        # Load DataFrame into PostgreSQL table
        df.to_sql(table_name, db, if_exists='replace', index=False)
        logging.info(f"Data loaded into the table {table_name} successfully!")
    except Exception as e:
        logging.error(f"Error loading data to PostgreSQL table: {e}")
