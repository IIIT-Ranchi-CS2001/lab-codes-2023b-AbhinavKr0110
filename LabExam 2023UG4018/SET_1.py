import numpy as np
import pandas as pd

data = pd.read_csv("AQI_Data.csv") #storing the aqi-dataset in data variable using read_csv

#common questions:
print(data.head(8)) #shows the first 8 rows
print(data.tail(5)) #shows the last 5 rows
print(data.info()) #dtype and number of non-null values in each column

data['AQI'] = pd.to_numeric(data['AQI'], errors='coerce')
data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce')
data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')
cityAQI = data.groupby('City')['AQI'].mean() #mean AQI by city
cityPM25 = data.groupby('City')['PM2.5'].max() #max PM2.5 by city
cityPM10 = data.groupby('City')['PM10'].min() #min PM10 by city
Each_city_data = pd.DataFrame({'Mean AQI': cityAQI, 'Max PM2.5': cityPM25, 'Min PM10': cityPM10})
print(Each_city_data)


#questions exclusive to set-1

#1.a
city_counts = np.unique(data['City'], return_counts=True)
city_counts_dict = dict(zip(city_counts[0], city_counts[1])) #zips the unqiue cities and number of rows corresponding to those cities and converts it into a dictionary
print(city_counts_dict) #the above created dictionary is displayed 

#1.b
pollutant_sums = np.sum(data[['PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2']], axis=1) #sums the pollutants and stores in 'pollutant_sums'
data['Total Pollutant Concentration'] = pollutant_sums #adds the total pollutant concentration field in the dataframe
data.to_csv('pollutant.txt', index=False) #makes the updated text file