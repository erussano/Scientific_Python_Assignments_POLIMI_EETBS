# -*- coding: utf-8 -*-
#Realized By: Enrico Russano
#N. matricola: 831952
#Assignment n.9 Date: 23/12/2017
#Demonstration of the share of each opaque component in the overall
#opaque heating and cooling load:
import pandas as pd
import matplotlib.pyplot as plt

items = [1,2,3]
labels= ["wall","ceiling","door"]
#I define the heating and cooling values from RLF Example 1:
HeatingLoadValues = [1149.2,1240,92.5]
CoolingLoadValues=[547.5,514.6,43]
cols=["r","b","g"]
plt.figure()
figure1=plt.pie(HeatingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
plt.figure()
figure2=plt.pie(CoolingLoadValues,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0), autopct='%1.1f%%')
#Arbitrary values of U_wall:
Uwall=[0.41,0.43,0.45,0.48,0.5]
Qwall=[]
Q_tot=[]
#I use a for loop to calculate the Q_value of each arbitrary U of the wall:
for U in Uwall:
    DT=24.8
    Awall=105.8
    Q=DT*Awall*U
    Qwall.append(Q)
    QTot=Q+1240+92.5
    Q_tot.append(QTot)
print Q_tot
print Qwall
plt.figure()
figure3=plt.plot(Uwall,Q_tot)
plt.xlabel("Uwall")
plt.ylabel("HeatingLoadValues")   
plt.show(figure3)