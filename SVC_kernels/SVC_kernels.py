#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:32:27 2020

@author: safir

Question: To do feature selection using Information Gain and Forward Selection, and to classify data using Linear, poly and rbf kernel.

Note: Check the Jupyter notebook file for structured flow
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_excel('Immunotherapy.xlsx')

X = dataset.drop(['Result_of_Treatment'], axis=1)
y = dataset['Result_of_Treatment']

# Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:, 0:] = sc.fit_transform(X[:, 0:])

'''
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest, SelectPercentile
print(dataset.head())

'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
'''

# Calculate Mutual Information between each feature and the target
mutual_info = mutual_info_classif(X.fillna(0), y)

# Create Feature Target Mutual Information Series
mi_series = pd.Series(mutual_info)
mi_series.index = X.columns
mi_series.sort_values(ascending=False)

mi_series.sort_values(ascending=False).plot.bar(figsize=(20,8))

# Select K best features
k_best_features = SelectKBest(mutual_info_classif, k=5).fit(X.fillna(0), y)
print('Selected top 5 features: {}'.format(X.columns[k_best_features.get_support()]))
features_selected = X.columns[k_best_features.get_support()]

# Using new features
X = dataset[features_selected].to_numpy()
y = y.to_numpy()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import KFold
kf = KFold(n_splits=10)
#print(kf.get_n_splits(X))

for train_index, test_index in kf.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    
# Training the classifier model on the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred)) 

from sklearn.model_selection import GridSearchCV 
  
# defining parameter range 
param_grid = {'C': [0.1, 1, 10, 100, 1000],  
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
              'kernel': ['rbf']}  
  
grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3) 
  
# fitting the model for grid search 
grid.fit(X_train, y_train) 

print(grid.best_params_) 
  
# print how our model looks after hyper-parameter tuning 
print(grid.best_estimator_) 


grid_predictions = grid.predict(X_test) 
  
# print classification report 
print(classification_report(y_test, grid_predictions)) 

# Training the classifier model on the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred)) 


# ROC
from sklearn import metrics
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred, pos_label=1)
auc = metrics.auc(fpr, tpr)
print("Area under the Curve : ", auc)

# Plotting AUC (Area Under the Curve)
from sklearn.metrics import roc_auc_score, roc_curve
ns_probs = [0 for _ in range(len(y_test))]
lr_probs = y_pred

ns_auc = roc_auc_score(y_test, ns_probs)
lr_auc = roc_auc_score(y_test, lr_probs)

print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))

# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)
# plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
# show the plot
plt.show()