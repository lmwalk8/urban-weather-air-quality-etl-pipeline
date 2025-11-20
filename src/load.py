from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import logging

def create_database_engine(db_url):
    """
    Creates a PostgreSQL database engine based on the Database URL

    Parameters:
        db_url: Specifically defined URL for a database

    Returns:
        engine (database engine): The PostgreSQL database engine.
    """
    try:
        engine = create_engine(db_url)
        return engine
    except Exception as e:
        logging.error(f"Error creating database engine: {e}")

def load_data_into_database_table(df, table_name, engine):
    """
    Loads data into table in PostgreSQL database.

    Parameters:
        df (pd.DataFrame): The data to be loaded into database table.
        table_name: Name of table the data will be loaded into.
        engine: The database engine where the table will be.
    """
    try:
        # Load DataFrame into PostgreSQL table
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"Data loaded into the table {table_name} successfully!")
    except Exception as e:
        logging.error(f"Error loading data to PostgreSQL table: {e}")

def read_existing_table(table_name, engine):
    """
    Reads data from existing table in PostgreSQL database.

    Parameters:
        table_name: Name of table the data will be selected from.
        engine: The database engine where the table will be.

    Returns:
        result (pd.DataFrame): The data from the table as a DataFrame.
    """
    try:
        # Read table data into DataFrame
        query = f"SELECT * FROM {table_name}"
        result = pd.read_sql(query, engine)
        result = result.replace({None: np.nan})
        logging.info(f"Data fetched from the existing table {table_name} successfully!")
        # Return results as DataFrame
        return result
    except Exception as e:
        logging.error(f"Error fetching data from PostgreSQL table: {e}")
        return None
