#!/usr/bin/env python
# coding: utf-8

# # Time Forecasting
# ### Algorithm: Random Forest
# ### Requirements: requirements.txt


import os.path
import pandas as pd
import numpy as np



from sklearn.model_selection import train_test_split#test_split
from sklearn.metrics import  accuracy_score         #test_score
from sklearn import tree                            #graphical file export
from sklearn.ensemble import RandomForestClassifier     #model

import joblib    #module used to make persistent model


if os.path.isfile('./train.csv')==False:
    print('Train Data not found')

dataset = pd.read_csv("train.csv")
dataset = dataset.fillna(dataset.mean())  #data loading
mtrdata= pd.to_numeric(dataset['mtr'])
X = dataset.drop(columns=['mtr'])
y = mtrdata                               #mtr= Max Time for Restoration (past)


#    Incidents: 1- thunderstorm
#               2- heavy-rain
#               3- tree-fall
#               4- transformer-fault
#               5- grid-fault

incidents_dict = {1:'thunderstorm', 2:'heavy-rain', 3:'tree-fall', 4:'transformer-fault', 5:'grid-fault'}

model = RandomForestClassifier()

def model_generation():
    return model.fit(X, y)


if os.path.isfile('./dump_model.jonlib')==True:
    joblib.load('dump_model.joblib')         #loading the saved model
else:
    model_generation()
    joblib.dump(model, 'dump_model.joblib')  #dumping model for persist


#prediction = model.predict([[1],[2],[3],[4],[5]]) #uncomment to view real-time forecast

def forecast():
    incident = input("Enter your issue [1 to 5] \n 1- thunderstorm \n 2- heavy-rain \n 3- tree-fall \n 4- transformer-fault \n 5- grid-fault \n \n")
    prediction = model.predict([[incident]])
    print(prediction[0])



#call this function for returning forecast of incident input
    
forecast()                                  
