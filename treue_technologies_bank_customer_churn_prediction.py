# -*- coding: utf-8 -*-
"""Treue Technologies / Bank_Customer_Churn_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16w-ZDZQ3sojnCUs6qbQmVzMRy9pBOUZ8

Name- Diksha Sharma

Task 1

Bank Customer Churn Prediction



The task is to train a machine learning model to predict whether a bank customer will churn (leave the bank) or not based on various customer attributes and banking behavior. The goal is to create a model that can accurately identify customers who are likely to churn, enabling proactive retention strategies.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/_Bank Customer Churn Prediction.zip")
df

"""EDA

"""

df.shape

df.head()

df.info()

"""Check null values in the dataset"""

df.isnull().sum()

df.size

"""Get overall statistics about dataset"""

df.describe()

"""Find shape of our dataset"""

df.shape

df.columns

df.drop(['RowNumber','CustomerId','Surname'],axis = 1,inplace = True)

df.tail()

"""Handling categorical columns"""

df['Geography'].unique()

df.replace({'France':0, 'Spain':1,'Germany':2}, inplace = True)

df['Gender'].unique()

df.replace({'Female':0, 'Male':1}, inplace = True)

df.head()

df['Exited'].value_counts()

sns.countplot(df['Exited'])
plt.show()

"""C:\Users\91932\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
  warnings.warn(
"""

df.columns

X = df[['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
       'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]
y = df['Exited']

"""Spliting the dataset into train and test set"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

len(X_train)

len(X_test)

"""Feature Scaling"""

from sklearn.preprocessing import StandardScaler

Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)
X_test = Scaler.transform(X_test)

X_train

"""Random forest classifier"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model

model_train = model.fit(X_train, y_train)
model_train

model_test = model.predict(X_test)
model_test

"""Model accuracy"""

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, model_test)
score