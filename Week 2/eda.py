# importing Pyhton Libraries for the task
from datetime import datetime
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

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
# print(data.nunique())

# To check only unique in single column
# print("\nWe are inspecting the column 'Location':\n\n",
#       data['Location'].unique())

# print("\nWe are inspecting the column 'Transaction Amount':\n\n",
#       data['TransactionAmount'].unique())

# print("\nWe are inspecting the column 'Purchase Date':\n\n",
#       data['PurchaseDate'].unique())

# Cleaning the dataset, check possibilities of null instances in the dataset
# print("\nConfirm number of null (empty cells) values int the dataset:\n\n",
#       data.nunique().isna().sum().sum())


# RFM Analysis

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
monetary_data.rename(
    columns={'TransactionAmount': 'MonetaryValue'}, inplace=True)
data = data.merge(monetary_data, on='CustomerID', how='left')
print("\nDisplay Data:\n", data.head())


# Calculating RFM Scores
# Establish the score
recency_scores = [5, 4, 3, 2, 1]
frequency_scores = [1, 2, 3, 4, 5]
monetary_scores = [1, 2, 3, 4, 5]

# Calculate the RFM scores
data['RecencyScore'] = pd.cut(
    data['Recency'], bins=5, labels=recency_scores)
data['FrequencyScore'] = pd.cut(
    data['Frequency'], bins=5, labels=frequency_scores)
data['MonetaryScore'] = pd.cut(
    data['MonetaryValue'], bins=5, labels=monetary_scores)


# Convert the data type into integers.
data['RecencyScore'] = data['RecencyScore'].astype(int)
data['FrequencyScore'] = data['FrequencyScore'].astype(int)
data['MonetaryScore'] = data['MonetaryScore'].astype(int)


# RFM Value Segmentation
# Calculate RFM score by combining the individual scores
data['RFM_Score'] = data['RecencyScore'] + \
    data['FrequencyScore'] + data['MonetaryScore']

# Create RFM segments based on the RFM score
segment_labels = ['Low-Value', 'Mid-Value', 'High-Value']
data['Value Segment'] = pd.qcut(data['RFM_Score'], q=3, labels=segment_labels)
print("\nShow RFM Data\n:", data.head())


# Segment Distribution
# RFM Segment Distribution
segment_counts = data['Value Segment'].value_counts().reset_index()
segment_counts.columns = ['Value Segment', 'Count']

pastel_colors = px.colors.qualitative.Pastel

# Create the bar chart
fig_segment_dist = px.bar(segment_counts, x='Value Segment', y='Count', color='Value Segment', color_discrete_sequence=pastel_colors,
                          title='RFM Value Segment Distribution')


# Update the layout
fig_segment_dist.update_layout(xaxis_title='RFM Value Segment',
                               yaxis_title='Count',
                               showlegend=False)

# display the visual/image/figure of the plotted data
fig_segment_dist.show()


# RFM Customer Segments
# create a new column for Customer Segments
data['RFM Customer Segments'] = ''


# Assigning RFM segments based on the RFM Score

data.loc[data['RFM_Score'] >= 9, 'RFM Customer Segments'] = 'Champions'
data.loc[(data['RFM_Score'] >= 6) & (data['RFM_Score'] < 9),
         'RFM Customer Segments'] = 'Potential Loyalists'
data.loc[(data['RFM_Score'] >= 5) & (data['RFM_Score'] < 6),
         'RFM Customer Segments'] = 'At Risk Customers'
data.loc[(data['RFM_Score'] >= 4) & (data['RFM_Score'] < 5),
         'RFM Customer Segments'] = "Can't Lose"
data.loc[(data['RFM_Score'] >= 3) & (data['RFM_Score'] < 4),
         'RFM Customer Segments'] = "Lost"


# Print the updated data with RFM segments
print(data[['CustomerID', 'RFM Customer Segments']])


segment_product_counts = data.groupby(
    ['Value Segment', 'RFM Customer Segments']).size().reset_index(name='Count')

segment_product_counts = segment_product_counts.sort_values(
    'Count', ascending=False)

fig_treemap_segment_product = px.treemap(segment_product_counts,
                                         path=['Value Segment', 'RFM Customer Segments'], values='Count',
                                         color='Value Segment', color_discrete_sequence=px.colors.qualitative.Pastel, title='RFM Customer Segments by Value')

fig_treemap_segment_product.show()


# Analyzing the distribution
champions_segment = data[data['RFM Customer Segments'] == 'Champions']

fig = go.Figure()
fig.add_trace(go.Box(y=champions_segment['RecencyScore'], name='Recency'))
fig.add_trace(go.Box(y=champions_segment['FrequencyScore'], name='Frequency'))
fig.add_trace(go.Box(y=champions_segment['MonetaryScore'], name='Monetary'))

fig.update_layout(title='Distribution of RFM Values within Champions Segment',
                  yaxis_title='RFM Value', showlegend=True)

fig.show()

# Build a correlation

correlation_matrix = champions_segment[[
    'RecencyScore', 'FrequencyScore', 'MonetaryScore']].corr()

# Visualize the correlation matrix using a heatmap
fig_heatmap = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu',
    colorbar=dict(title='Correlation')
))

fig_heatmap.update_layout(
    title='Correlation Matrix of RFM Values within Champions Segment')

fig_heatmap.show()
