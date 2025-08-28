import pandas as pd
import logging

def extract_weather_data():
    """
    Fetches weather and air quality data from the local CSV.

    Returns:
        df (pd.DataFrame): The weather and air quality data in a DataFrame.
    """
    logging.info("Attempting to extract all weather and air quality data from CSV")

    try:
        df = pd.read_csv("UrbanAirQualityandHealthImpactDataset.csv")
        logging.error("Successfully extracted the data")
        return df
    except Exception as e:
        logging.error(f"Extraction failed for the CSV file: {e}")
        return pd.DataFrame()
