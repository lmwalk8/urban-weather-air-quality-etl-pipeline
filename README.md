# Urban Weather & Air Quality ETL Pipeline

This project shows how to use an ETL (extract, transform, load) pipeline on a dataset of weather and air quality data. After going through the pipeline (written in Python), the processed data is used for analysis in Jupyter notebooks.

## Project Overview:

- Extract weather and air quality data from UrbanAirQualityandHealthImpactDataset.csv.
- Transform raw data using Python pandas library by removing or replacing missing data, dropping duplicate data, correctly converting datetime data, and placing the newly cleaned data into two DataFrames (weather, air quality) to be used for separate analyses.
- Load processed data into separate PostgreSQL database tables.
- Test that the pipeline works as intended using pytest.
- Analyze the processed data through tables and charts in Jupyter notebooks.

## Technology Stack (Prerequisites to Run Project):

- Programming Language: Python
    - Libraries Used:
        - `pandas`: For data manipulation and analysis.
        - `SQLAlchemy`: For PostgreSQL interactions.
        - `numpy`: For quick mathematical operations.
        - `dotenv`: For environment variables (DB credentials).
        - `matplotlib`: For creating a variety of 2D plots/charts.
        - `seaborn`: For more complex visualizations of data.
        - `pytest`: For testing ETL pipeline steps.
    - Database: PostgreSQL
    - Dataset Source: [Urban Air Quality and Health Impact Dataset](https://www.kaggle.com/datasets/abdullah0a/urban-air-quality-and-health-impact-dataset)

## Steps for Project Setup:

1. Clone this repository:
```
git clone https://github.com/lmwalk8/urban-weather-air-quality-etl-pipeline.git
cd urban-weather-air-quality-etl-pipeline
```

2. Create and activate a Python virutal environment:
```
python3 -m venv air_quality_project_env
source air_quality_project_env/bin/activate (Linux/macOS) OR air_quality_project_env\Scripts\activate.bat (Windows)
```

3. Install all required dependencies:
`pip install -r requirements.txt`

4. Set up required environment variables:
```
Create .env variable in project directory and add this database information:
DATABASE_URL=postgresql://your_user:your_password@host:port/database_name
```

Now all ETL methods should be able to run in the tests and notebooks, leading to clean data that can be used in further analyses.
