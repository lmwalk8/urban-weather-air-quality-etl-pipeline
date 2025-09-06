from sqlalchemy import create_engine, select
import logging

def create_database_engine(db_url):
    """
    Creates a PostgreSQL database engine based on the Database URL

    Parameters:
        db_url: Specifically defined URL for a database

    Returns:
        db (database engine): The PostgreSQL database engine.
    """
    try:
        engine = create_engine(db_url)
        return engine
    # engine.dispose()
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
    # engine = create_database_engine()

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
    """
    try:
        # Connect to database engine
        connection = engine.connect()
        # Select all rows in table
        select_rows = select(table_name)
        result = connection.execute(select_rows)
        # Fetch results
        for row in result:
            print(row)
        logging.info(f"Data fetched from the existing table {table_name} successfully!")
        # Close database connection
        connection.close()
    except Exception as e:
        logging.error(f"Error fetching data from PostgreSQL table: {e}")
