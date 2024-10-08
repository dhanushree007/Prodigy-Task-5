# -*- coding: utf-8 -*-
"""Prodigy-Task5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b_uuSOxh6J_KbNbdXZeC41xNsl9Asiaf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('US_Accident.csv')

# View the first few rows
df.head()

df.isnull().sum()

df.info()

df.shape

# Drop or fill missing values
df['Precipitation(in)'].fillna(0, inplace=True)  # Fill missing precipitation with 0 (no precipitation)
df.dropna(subset=['Weather_Condition', 'Temperature(F)', 'Visibility(mi)', 'Start_Lat', 'Start_Lng'], inplace=True)

df.dtypes

# Plot accidents by weather condition
plt.figure(figsize=(12,6))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar', color='green')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Visualize severity vs road conditions
road_conditions = ['Bump', 'Crossing', 'Traffic_Signal', 'Stop', 'Junction']
severity_by_road = df.groupby(road_conditions)['Severity'].mean().reset_index()

# Plot
plt.figure(figsize=(10,6))
severity_by_road.set_index(road_conditions).plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Average Severity by Road Conditions')
plt.ylabel('Average Severity')
plt.show()

import folium
from folium.plugins import HeatMap

# Create a base map centered in the US
map_center = [df['Start_Lat'].mean(), df['Start_Lng'].mean()]
m = folium.Map(location=map_center, zoom_start=5)

# Get coordinates for the accident locations
heat_data = [[row['Start_Lat'], row['Start_Lng']] for index, row in df.iterrows()]

# Add heatmap to the map
HeatMap(heat_data).add_to(m)

# Save the map to an HTML file and display it
m.save('accident_heatmap.html')
m  # To display in a notebook

# Select relevant columns for correlation
correlation_cols = ['Severity', 'Temperature(F)', 'Humidity(%)', 'Visibility(mi)', 'Precipitation(in)']
df_corr = df[correlation_cols].dropna()

# Correlation matrix
corr_matrix = df_corr.corr()

# Plot correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Between Severity and Weather Factors')
plt.show()

# Plot the distribution of accident severity
plt.figure(figsize=(8,6))
sns.countplot(x='Severity', data=df, palette='coolwarm')
plt.title('Accident Severity Distribution')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# Group by Weather Condition and Severity
weather_severity = df.groupby(['Weather_Condition', 'Severity']).size().unstack().fillna(0)

# Plot a heatmap
plt.figure(figsize=(12,6))
sns.heatmap(weather_severity, cmap='coolwarm', annot=True, fmt='.0f', linewidths=0.5)
plt.title('Accident Severity by Weather Condition')
plt.ylabel('Weather Condition')
plt.xlabel('Severity Level')
plt.xticks(rotation=45)
plt.show()

# Plot accidents by state
plt.figure(figsize=(12,6))
sns.countplot(x='State', data=df, order=df['State'].value_counts().index, palette='viridis')
plt.title('Accident Count by State')
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.show()

# Group by Visibility and Severity
df['Visibility_bins'] = pd.cut(df['Visibility(mi)'], bins=[0, 1, 2, 5, 10, 20], labels=['0-1', '1-2', '2-5', '5-10', '10+'])

plt.figure(figsize=(10,6))
sns.countplot(x='Visibility_bins', hue='Severity', data=df, palette='Set2')
plt.title('Accidents by Visibility Levels')
plt.xlabel('Visibility (mi)')
plt.ylabel('Number of Accidents')
plt.show()

# Plot accidents during day and night
plt.figure(figsize=(8,6))
sns.countplot(x='Sunrise_Sunset', data=df, palette='coolwarm')
plt.title('Accidents During Day vs. Night')
plt.xlabel('Time of Day (Sunrise vs. Sunset)')
plt.ylabel('Number of Accidents')
plt.show()

# Bin wind speed for easier visualization
df['Wind_Speed_bins'] = pd.cut(df['Wind_Speed(mph)'], bins=[0, 10, 20, 30, 40, 50, 60], labels=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60'])

plt.figure(figsize=(10,6))
sns.countplot(x='Wind_Speed_bins', hue='Severity', data=df, palette='coolwarm')
plt.title('Accidents by Wind Speed and Severity')
plt.xlabel('Wind Speed (mph)')
plt.ylabel('Number of Accidents')
plt.show()

# Bin temperatures for better visualization
df['Temperature_bins'] = pd.cut(df['Temperature(F)'], bins=[-10, 0, 30, 50, 70, 90, 110], labels=['-10-0', '0-30', '30-50', '50-70', '70-90', '90+'])

plt.figure(figsize=(10,6))
sns.countplot(x='Temperature_bins', hue='Severity', data=df, palette='RdYlBu')
plt.title('Accidents by Temperature and Severity')
plt.xlabel('Temperature (F)')
plt.ylabel('Number of Accidents')
plt.show()

"""#Insights from Data Visualisation

Weather Conditions: Specific weather conditions like rain, fog, or snow might contribute to accidents.

Road Conditions: Elements like traffic signals, bumps, and junctions can play a role in accident severity.

Accident Hotspots: By visualizing the data on a map, we can identify areas with high accident frequency.

The visualizations reveal that **accident severity is significantly influenced by factors such as weather conditions (e.g., more severe accidents in poor visibility and bad weather), time of day (higher accident counts during nighttime), and environmental factors like wind speed and temperature**, with accidents occurring more frequently in moderate weather but showing high severity under extreme conditions (e.g., high winds and freezing temperatures). Additionally, **geographic regions (states) and seasons also play a role in accident frequency, with certain states exhibiting more hotspots, especially during specific times of the year**.
"""