# -*- coding: utf-8 -*-
"""Sonar vs Rock Mine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1twjIZ9OShyybwmPvjMwer4ffJCRfIYSF

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Preprocessing"""

sonar_data = pd.read_csv('/content/sonar data.csv',header=None)

sonar_data.head()
#head displays first 5 rows

#no.of rows and columns
sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()
#60 represents column number which contains R or M

sonar_data.groupby(60).mean()

#separating data and label
x = sonar_data.drop(columns=60,axis = 1)
y = sonar_data[60]

print(x)
print(y)

"""Training and test data"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1,stratify=y,random_state = 1)

print(x.shape,x_train.shape,x_test.shape)

print(x_train)
print(y_train)

"""Model Training --> LOGISTIC REGRESSION"""

model = LogisticRegression()

#training the model
model.fit(x_train, y_train)

"""Model Evaluation"""

#accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction,y_train)

print("Accuracy : " ,training_data_accuracy)

#accuracy on test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction,y_test)

print("Accuracy on test data: ", test_data_accuracy)

"""Making Predictive system"""

input_data = (0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115)
#changing to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instances
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print("The object is a rock")
else:
  print("The object is a Mine")





