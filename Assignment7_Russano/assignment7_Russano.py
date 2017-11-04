# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.7 Date: 4/11/2017
#Calculating of the beam irradiation, the diffuse irradiation, and the PXI for the city of Piacenza
import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\utente\Desktop\Building Systems\MyNewPandas")
#I read the total window DataFrame:
windows_DF= pd.read_csv("windows.csv",sep=";", index_col=0) 
#Define the latitude location of Piacenza:
latitude_location= 45
#Read the Beam Irradiance as DataFrame:
B_Irr_DF= pd.read_csv("BeamIrradiance.csv",sep=";",index_col=1)
#Read the Diffuse Irradiance as DataFrame:
D_Irr_DF= pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=1)
#Relative to the East window:
index= "E"
#Calculating the ED value (Beam Irr):
ED_value=B_Irr_DF[str(latitude_location)][index]
#Calculating the Ed value (Diff Irr):
Ed_value=D_Irr_DF[str(latitude_location)][index]
#Calculating the PXI of eastern window without external shading:
PXI_east=ED_value+Ed_value

windows_DF["PXI"]=np.array([PXI_east,0,0,0])
windows_DF.to_csv("windows_completedwithPXI.csv",sep=";")

