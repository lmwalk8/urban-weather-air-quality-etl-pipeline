import pandas as pd
import logging

def transform_data(df):
    """
    Transform the raw weather data into a structured DataFrame.

    Parameters:
        df (pd.DataFrame): The combinded weather and air quality data.

    Returns:
        weather_df (pd.DataFrame): The transformed weather data in a DataFrame.
        air_quality_df (pd.DataFrame): The transformed air quality data in a DataFrame.
    """
    weather_df = df["temp"]
    air_quality_df = df["score"]

    return weather_df, air_quality_df