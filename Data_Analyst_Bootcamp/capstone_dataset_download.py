import pandas as pd
from numpy import nan as NA
from datetime import datetime
import os

# Path to file location
dataset = pd.read_csv(
    "D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv")

# Finding total number of datasets
print("Total Column and Total Rows: \n")
print(dataset.shape)  # 5719877rows #13 columns

# Finding out top 5 column names
print("Find Out Top 5 Rows: \n")
print(dataset.head(5))

# Finding out column names
print("Find Out More About Column: \n")
print(dataset.columns)

# Finding respective data types
print(dataset.dtypes)

# Finding null values.
print("Total missing values in each column: \n")
missing_values = dataset.isnull().sum()
print(missing_values)


# Preparing an Array(s) of columns to Fill out Missing Values
non_numeric_cols = ['start_stion_name', 'end_station_name']

numeric_cols = ['start_stion_id', 'end_stion_id', 'end_lat', 'end_lng']

# Convert the two columns (started_at and ended_at) to date
dataset['started_at', 'ended_at'] = pd.to_datetime(
    dataset['started_at', 'ended_at'], utc=True)


# Split time from date for the two columns (started_at and ended_at)


# # Define the directory where your CSV files are located
directory = 'D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv'

# # List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# # Read and concatenate all CSV files into one DataFrame
combined_data = pd.concat(
    [pd.read_csv(os.path.join(directory, file)) for file in csv_files])

# # Save the combined data to a new CSV file
combined_data.to_csv('combined_data.csv', index=False)

combined_data.to_csv(
    'D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv', index=False)
# # print()
