import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime

# Loading our dataset to conduct EDA
data = pd.read_csv("D:/Data Science BootCamp/Week 2/rfm_data.csv")
# print(data.describe())

# print(data.shape())

# Display number of columns
# print(data.columns)

# Display first 5 rows
# print(data.head())

# Display total columns and rows of the data set
# print(data.shape)  # The dataset contain 1000 rows and 6 columns

# Print unique about the dataset
print(data.nunique())

# To check only unique in single column
# print("\nWe are inspecting the column 'Location':\n\n",
#       data['Location'].unique())

# print("\nWe are inspecting the column 'Transaction Amount':\n\n",
#       data['TransactionAmount'].unique())

# print("\nWe are inspecting the column 'Purchase Date':\n\n",
#       data['PurchaseDate'].unique())

# Cleaning the dataset, check possibilities of null instances in the dataset
print("\nConfirm number of null (empty cells) values int the dataset:\n\n",
      data.nunique().isna().sum().sum())

# Convert 'PurchaseDate' to datetime
data['PurchaseDate'] = pd.to_datetime(data["PurchaseDate"])

# Calculate Recency
data['Recency'] = (datetime.now().date() - data['PurchaseDate'].dt.date)

# Calculate Frequency
frequency_data = data.groupby('CustomerID')['OrderID'].count().reset_index()
frequency_data.rename(columns={'OrderID': 'Frequency'}, inplace=True)
data = data.merge(frequency_data, on='CustomerID', how='left')

# Calculate Monetary
monetary_data = data.groupby('CustomerID')[
    'TransactionAmount'].sum().reset_index()
