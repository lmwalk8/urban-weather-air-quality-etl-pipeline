import pandas as pd
import logging

def transform_data(df):
    """
    Transform the raw weather data into two structured DataFrames.

    Parameters:
        df (pd.DataFrame): The combinded weather and air quality data.

    Returns:
        weather_df (pd.DataFrame): The transformed weather data in a DataFrame.
        air_quality_df (pd.DataFrame): The transformed air quality data in a DataFrame.
    """
    df_transformed = df.copy()
    logging.info("Transforming the weather and air quality data...")

    # Fill missing values
    df_transformed['preciptype'] = df_transformed['preciptype'].fillna('None')
    df_transformed['stations'] = df_transformed['stations'].fillna('N/A')
    df_transformed['Condition_Code'] = df_transformed['Condition_Code'].fillna(-1)
    df_transformed['snowdepth'] = df_transformed['snowdepth'].fillna(0)

    # Remove duplicates
    df_transformed = df_transformed.drop_duplicates()
    
    # Convert to datetime objects
    df_transformed['datetime'] = pd.to_datetime(df_transformed['datetime'])
    df_transformed['sunrise'] = pd.to_datetime(df_transformed['sunrise'])
    df_transformed['sunset'] = pd.to_datetime(df_transformed['sunset'])

    # Define weather-related columns
    weather_columns = [
        'datetime', 'datetimeEpoch', 'tempmax', 'tempmin', 'temp',
        'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity',
        'precip', 'precipprob', 'precipcover', 'preciptype', 'snow', 'snowdepth',
        'windgust', 'windspeed', 'winddir', 'pressure', 'cloudcover',
        'visibility', 'solarradiation', 'solarenergy', 'uvindex', 'severerisk',
        'sunrise', 'sunriseEpoch', 'sunset', 'sunsetEpoch', 'moonphase',
        'conditions', 'description', 'icon', 'stations', 'source', 'City',
        'Temp_Range', 'Heat_Index', 'Month', 'Season', 'Day_of_Week', 'Is_Weekend'
    ]
    
    # Define air quality-related columns
    air_quality_columns = [
        'datetime', 'City', 'Severity_Score', 'Condition_Code', 'Health_Risk_Score',
        'Month', 'Season', 'Day_of_Week', 'Is_Weekend'
    ]
    
    # Create separate dataframes
    weather_df = df_transformed[[col for col in weather_columns if col in df_transformed.columns]].copy()
    air_quality_df = df_transformed[[col for col in air_quality_columns if col in df_transformed.columns]].copy()

    logging.info("Weather and air quality data transformed successfully into two separate DataFrames!")
    return weather_df, air_quality_df
