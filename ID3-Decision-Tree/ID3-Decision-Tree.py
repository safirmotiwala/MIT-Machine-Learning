#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:12:16 2020

@author: safir

@status: Entropy and Gain for Root Node Done
            Sub Tree Next
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('house-votes-84.csv')
party = {'republican':0, 'democrat':1}
vote = {'y':0, 'n':1, '?':2}

for col in dataset.columns:
    if col != 'party':
        dataset[col] = dataset[col].map(vote)
dataset['party'] = dataset['party'].map(party)

X = dataset.iloc[:, 1:17].values
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import KFold
kf = KFold(n_splits=5)
#print(kf.get_n_splits(X))

for train_index, test_index in kf.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    
# Training the Decision Tree Classification model on the Training set
'''
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(random_state = 0)
classifier.fit(X_train, y_train)
'''

'''
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Testing the Accuracy
print("Training accuracy: {} %".format(np.multiply(classifier.score(X_train,y_train), 100)))
print("Test Accuracy: {} %".format(np.multiply(classifier.score(X_test,y_test),100)))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
'''

# Building the Decision Tree Model with Information Gain

from information_gain import information_gain
ig = information_gain(X_train, y_train)
ig.add_features(dataset)
print(ig.features)

ig.total_entropy_find(dataset)

## Making the decision Tree
ig.decision_tree()