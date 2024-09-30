# Prodigy-Task-5

## Project: US Accident Data Analysis

### Overview
This project analyzes a dataset of traffic accidents that occurred across the United States. It involves data cleaning, preprocessing, and visualizations to uncover trends related to accident severity, weather conditions, geographic hotspots, and other factors.

### Dataset
The dataset used in this project is the **US_Accident.csv** file, which contains information on various accidents, including details on weather, location, visibility, severity, and road conditions.

### Prerequisites
- Python 3.x
- Libraries: Pandas, Numpy, Matplotlib, Seaborn, Folium, TextBlob, WordCloud, Scikit-learn

Install the necessary libraries via pip:
```bash
pip install pandas numpy matplotlib seaborn folium textblob wordcloud scikit-learn
```

### Data Preprocessing
1. **Loading the dataset**: The dataset is loaded using Pandas and the initial steps involve exploring the dataset's structure.
2. **Handling Missing Values**: 
   - Missing precipitation values were filled with 0 (assuming no precipitation).
   - Missing values in critical columns like `Weather_Condition`, `Temperature(F)`, and `Visibility(mi)` were dropped.
3. **Data Types**: Data types were checked and handled accordingly for further analysis.

### Data Analysis & Visualizations
1. **Accident Trends by Weather Conditions**: 
   - Visualized the top 10 weather conditions during accidents using a bar chart.
2. **Severity vs. Road Conditions**: 
   - Analyzed how different road features like bumps, junctions, and traffic signals impact accident severity.
3. **Heatmap of Accidents**: 
   - Used Folium to create a heatmap that visualizes accident hotspots across the U.S.
4. **Correlation Analysis**: 
   - Examined correlations between weather-related factors (temperature, humidity, visibility) and accident severity using a heatmap.
5. **Severity Distribution**: 
   - Analyzed the distribution of accidents by severity level.
6. **Weather Condition & Severity Heatmap**: 
   - Explored the relationship between weather conditions and accident severity using a heatmap.
7. **Accidents by State**: 
   - Counted and visualized the number of accidents per state.
8. **Accidents by Visibility**: 
   - Investigated how visibility conditions influence accident severity.
9. **Day vs. Night Accidents**: 
   - Compared accident frequencies during day and night.
10. **Accidents by Wind Speed**: 
    - Studied the impact of wind speed on accident severity.
11. **Accidents by Temperature**: 
    - Binned temperatures and visualized the relationship between temperature ranges and accident severity.

### Insights
1. **Weather Conditions**: Certain weather conditions such as fog, rain, and snow are associated with higher accident frequencies and severity.
2. **Road Conditions**: Features like traffic signals, bumps, and junctions significantly influence accident severity.
3. **Accident Hotspots**: There are specific geographic regions with higher accident frequencies.
4. **Weather, Visibility, and Severity**: Poor visibility and harsh weather conditions tend to result in more severe accidents.
5. **State-Wise Trends**: Different states show varying accident trends, likely due to environmental and infrastructural differences.

### Usage
The notebook allows users to:
1. **Visualize accident trends** based on weather, road conditions, time of day, and geographic location.
2. **Generate heatmaps** to identify accident hotspots.
3. **Analyze the severity** of accidents in relation to weather and road conditions.

### Conclusion
The project provides valuable insights into how environmental factors like weather, visibility, and road conditions impact accident severity. It highlights the need for targeted safety measures in regions and conditions prone to severe accidents.

