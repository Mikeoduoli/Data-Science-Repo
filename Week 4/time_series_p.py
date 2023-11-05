# Importing libraries necessary for our project (Time Series Modeling)
import pandas as pd
import numpy as np


# Load Data
data = pd.read_csv(
    'D:/Data Science BootCamp/Week 4/craigslist_vehicles.csv')

# convert to data frame
# data = pd.read_excel(data_set)

data.head(5)
