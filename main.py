# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:46:29 2019

@author: Jonas Rusiana
"""
# testing out github.dev thing - turon
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('household_power_consumption.csv')
test_dataset = pd.read_csv('test.csv')
dataset.isnull().any()
dataset = dataset.fillna(method='ffill')

X = dataset[['Global_active_power','Global_reactive_power','Voltage','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']]
y = dataset['sub_metering_4']
test_pred = test_dataset[['Global_active_power','Global_reactive_power','Voltage','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

print("AI Electricity Usage Predictor Terminal v0.1")
print("Author: Jonas Rusiana")
print("MIT License")
print("Type 'License' to learn more")

while True:
    command = input(str(">> ")).lower()
    if command == "exit":
        print("exiting...")
        break
    elif command == "help":
        print("Commands : Syntax")
        print("predict -[options] : -t use training data.  -n predicts a new data using the test.csv file, note: edit the test.csv file if you want to predict new data.")
        print("exit : exits the program.")
        continue
    elif command == "predict":
        print("Options: -t use training data. -n predicts a new data using the test.csv file, note: edit the test.csv file if you want to predict new data.")
    elif command == "predict -n":
        new_pred = test_pred
        new_prediction = regressor.predict(test_pred)
        print(new_prediction)
    elif command == "predict -t":
        print(df1)

        df1.plot(kind='bar',figsize=(10,8))
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()
        
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        
        new_pred = test_pred
        
        new_prediction = regressor.predict(test_pred)
        
        print(new_prediction)
    elif command == "license":
        print("License used: MIT License")
        print("The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology. As a permissive license, it puts only very limited restriction on reuse and has, therefore, an excellent license compatibility.")
    else:
        print("Unrecognized command '%s'" % (command))
        continue
