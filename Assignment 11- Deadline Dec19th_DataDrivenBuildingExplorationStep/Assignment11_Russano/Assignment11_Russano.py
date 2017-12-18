# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.11 (ultimate) Date: 18/12/2017

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath= ("C:\Users\utente\Desktop\Assignment11_Russano\Data")
ConsumptionFileName = "consumption_5545.csv"
ConsumptionFilePath= DataFolderPath+"/"+ConsumptionFileName
DF_consumption = pd.read_csv(ConsumptionFilePath,sep=",",index_col=0)
previousIndex1= DF_consumption.index
NewparsedIndex1 = pd.to_datetime(previousIndex1)
DF_consumption.index= NewparsedIndex1
DF_myChosenDate = DF_consumption["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_myChosenDate.describe()

DF_myChosenDate.plot()
plt.xlabel('Time')
plt.ylabel('AC Power [W]')
plt.show()

weatherSourceFileName = "Austin_weather_2014.csv"
weatherSourceFilePath = DataFolderPath+"/"+weatherSourceFileName
DF_weather_source = pd.read_csv(weatherSourceFilePath,sep = ";",index_col=0)
previousIndex_weather_Source = DF_weather_source.index
NewparsedIndex_weather_Source = pd.to_datetime(previousIndex_weather_Source)
DF_weather_source.index= NewparsedIndex_weather_Source
series_temperature=DF_weather_source["temperature"]
#Now i would prefer to have it as Dataframe with just one column:
DF_temperature = DF_weather_source[["temperature"]]

#I do the same for Irradiation:
IrradianceSourceFileName = "irradiance_2014_gen.csv"
IrradianceSourceFilePath = DataFolderPath+"/"+IrradianceSourceFileName
DF_irradiance_source = pd.read_csv(IrradianceSourceFilePath,sep = ";",index_col=1)
# If I want to take just the column "gen":
DF_Irradiance=DF_irradiance_source[["gen"]]
previousIndex_IrradianceSource= DF_irradiance_source.index
NewparsedIndex_IrradianceSource = pd.to_datetime(previousIndex_IrradianceSource)
DF_irradiance_source.index= NewparsedIndex_IrradianceSource
DF_JunefirstTillThird= DF_irradiance_source["2014-06-01 00:00:00":"2014-06-03 23:00:00"]
DF_joined=DF_consumption.join([DF_temperature,DF_Irradiance])
DF_joined.dropna()

DF_chosen_dates = DF_joined['2014-06-01':'2014-06-03']
DF_chosen_dates.plot()

fig = plt.figure()
axis_1= fig.add_subplot(111) #axis for consumption
axis_2= axis_1.twinx()  #axis for temperature
axis_3= axis_1.twinx()  #axis for solar irradiance
rspine = axis_3.spines['right']
consum_col = 'air conditioner_5545'

DF_chosen_dates.plot(ax=axis_1, y=consum_col, legend=False,color='b')
axis_1.set_ylabel('Consumption',color='b')
axis_1.tick_params(axis='y', colors='b')

DF_chosen_dates.plot(ax=axis_2, y='temperature', legend=False, color='g')
axis_2.set_ylabel('Temperature deg C',color='g')
axis_2.tick_params(axis='y',colors='g')

DF_chosen_dates.plot(ax=axis_3,y='gen',legend=False,color='r')
axis_3.set_ylabel('Irradiance [from PV]',color='r')
axis_3.tick_params(axis='y',colors='r')

axis_1.set_xlabel('Time')
plt.show()







