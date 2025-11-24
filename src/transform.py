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
    # Replace list values like ['rain'] with 'rain', then fill NaN with 'None'
    df_transformed['preciptype'] = df_transformed['preciptype'].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) > 0 else x
    ).fillna('None')
    df_transformed['stations'] = df_transformed['stations'].fillna('N/A')
    df_transformed['Condition_Code'] = df_transformed['Condition_Code'].fillna(-1)
    df_transformed['snowdepth'] = df_transformed['snowdepth'].fillna(0)

    # Remove duplicates
    df_transformed = df_transformed.drop_duplicates()
    
    # Convert to datetime objects
    df_transformed['datetime'] = pd.to_datetime(df_transformed['datetime'], errors='coerce')
    df_transformed['sunrise'] = _parse_datetime(df_transformed['sunrise'])
    df_transformed['sunset'] = _parse_datetime(df_transformed['sunset'])

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

def _parse_datetime(series):
    """
    Parse a column that may contain either full datetime strings or only HH:MM:SS values.
    """
    if pd.api.types.is_datetime64_any_dtype(series):
        return series

    series_str = series.astype('string')
    time_mask = series_str.str.match(r'^\d{1,2}:\d{2}:\d{2}$', na=False)

    parsed = pd.Series(pd.NaT, index=series.index, dtype='datetime64[ns]')

    if time_mask.any():
        parsed.loc[time_mask] = pd.to_datetime(
            series_str.loc[time_mask],
            format='%H:%M:%S',
            errors='coerce'
        )

    if (~time_mask).any():
        parsed.loc[~time_mask] = pd.to_datetime(
            series_str.loc[~time_mask],
            errors='coerce'
        )

    return parsed
