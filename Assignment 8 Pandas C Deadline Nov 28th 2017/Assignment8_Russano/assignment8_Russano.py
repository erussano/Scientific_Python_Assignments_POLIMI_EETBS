# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.8 Date: 26/11/2017
#Calculating of the beam irradiation, the diffuse irradiation, and the PXI for any city given its Irradiance:
import os
import pandas as pd
import numpy as np
os.chdir("C:\Users\utente\Desktop\Building Systems\MyNewPandas")
#I import scipy in order to interpolate:
import scipy as sp 

#I define the function that calculating PXI values from latitudes and orientation of the wall:
def PXI_finder (Direction,Latitude):

    B_Irr_DF= pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
    D_Irr_DF= pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)
    #Interpolation:
    name_of_columns=B_Irr_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    #Calculating the ED value (Beam Irr):
    ED=sp.interp(Latitude, name_of_columns_as_numbers,B_Irr_DF.loc[Direction])
    #Calculating the Ed value (Diff Irr):
    Ed=sp.interp(Latitude, name_of_columns_as_numbers,D_Irr_DF.loc[Direction])
    #Calculating the PXI of windows without external shading:
    PXI=ED+Ed
    return PXI
    
#I read the total window DataFrame:
windows_DF= pd.read_csv("windows.csv",sep=";", index_col=0) 
Latitude_location=45
    
PXI_values=[]
for i in windows_DF.index.tolist():
    print i
    PXI_values = np.append(PXI_values,PXI_finder(windows_DF["Direction"][i],Latitude_location))
    
windows_DF["PXI"]= PXI_values*windows_DF["Tx"]

windows_DF.to_csv("windows_completed_withPXI.csv",sep=";") 


