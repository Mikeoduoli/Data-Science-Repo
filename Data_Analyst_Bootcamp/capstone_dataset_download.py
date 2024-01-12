import pandas as pd
from numpy import nan as NA
from datetime import datetime
import os

# Path to file location
dataset = pd.read_csv(
    "D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv")

# Finding total number of datasets
# print("Total Rows Columns: \n")
# print(dataset.shape)  # 5719877rows #13 columns

# Finding out top 5 column names
print("Find Out Top 5 Rows: \n")
print(dataset.head(5))

# Finding out column names
# print("Find Out More About Column: \n")
# print(dataset.columns)

# Finding respective data types
# print(dataset.dtypes)

# Finding null values.
# print("Total missing values in each column: \n")
# missing_values = dataset.isnull().sum()
# print(missing_values)


# Preparing an Array(s) of columns to Fill out Missing Values
non_numeric_cols = ['start_station_name', 'end_station_name']

numeric_cols = ['start_station_id', 'end_station_id', 'end_lat', 'end_lng']

# Create a for Loop to iterate through the array
# for col in non_numeric_cols:
#     filled_cols = dataset[col].fillna('N/A')
# print("Filled Empty cells: \n")
# print(filled_cols.isnull().sum())

# Instead of running the above longer for loop, use a list comprehession
existing_column_to_be_filled = [
    cols for cols in non_numeric_cols if cols in dataset.columns]

numeric_column_to_be_filled = [
    col for col in numeric_cols if col in dataset.columns]

# Now fill the empty cells with "N/A"
# filled_empty_cells = dataset.fillna(
#     value='N/A', Columns=existing_column_to_be_filled)

# Instead of running the above longer For Loop, use list comprehession technique
filled_dataset = pd.DataFrame({
    cols: dataset[cols].fillna(
        'N/A', inplace=True) if cols in existing_column_to_be_filled else dataset[cols]
    for cols in dataset.columns
})

print("\nFilled Empty cells: \n")
print(filled_dataset.isnull().sum())

# ---------------------------------------------------------------------------
# For Numeric columns
# Instead of running the above longer For Loop, use list comprehession technique
filled_dataset_numeric = pd.DataFrame({
    col: dataset[col].fillna(
        0, inplace=True) if col in numeric_column_to_be_filled else dataset[col]
    for col in dataset.columns
})

print("\nFilled Numeric Empty cells: \n")
print(filled_dataset_numeric.isnull().sum())

# ---------------------------------------------------------------------------

# Create a function to execute the filling across the empty cells


def fill_all_cols(dataset):

    non_numeric_cols = ['start_station_name', 'end_station_name']
    dataset[non_numeric_cols] = dataset[non_numeric_cols].fillna(value='N/A')

    numeric_cols = ['start_station_id',
                    'end_station_id', 'end_lat', 'end_lng']
    dataset[numeric_cols] = dataset[numeric_cols].fillna(value=0)

    return dataset


dataset = fill_all_cols(dataset)

print("\nConfirming Filled Cells: \n")
print(dataset.isnull().sum())

# Now your clean dataset is ready for export
# dataset.to_csv(
#     'D:/Capstone_Bike_Share_Analysis/datasets/clean_bike_data.csv', index=False)
# print()


# Fill the non_numeric_cols with "NA"
# new_dataset = non_numeric_cols.fillna("N/A")
# print("Filled Empty cells: \n")
# print(new_dataset.isnull().sum())

# data = {'start_stion_at': [], 'end_station_name': []}
# for col in non_numeric_cols:
#     data[col] = ['NA']*len(data)

# for col, values in data.items():
#     print("Columns Filled with NA: \n")
#     print(col, values)


# Convert the two columns (started_at and ended_at) to date
# dataset['started_at', 'ended_at'] = pd.to_datetime(
#     dataset['started_at', 'ended_at'], utc=True)


# Split time from date for the two columns (started_at and ended_at)


# # Define the directory where your CSV files are located
# directory = 'D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv'

# # List all CSV files in the directory
# csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# # Read and concatenate all CSV files into one DataFrame
# combined_data = pd.concat(
# [pd.read_csv(os.path.join(directory, file)) for file in csv_files])

# # Save the combined data to a new CSV file
# combined_data.to_csv('combined_data.csv', index=False)

# combined_data.to_csv(
#     'D:/Capstone_Bike_Share_Analysis/datasets/datasets/all_cleaned.csv', index=False)
# # print()
