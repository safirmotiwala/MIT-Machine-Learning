#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:30:47 2020

@author: safir
"""

import numpy as np

class FindS:
    def __init__(self):
        self.Xtrain = ""
        self.ytrain = ""
        self.Xtest = ""
        self.ytest = ""
        self.specific_hypothesis = []
    
    def fit(self, X, y):
        count = 0
        self.Xtrain, self.ytrain = X, y
        for i, val in enumerate(y):
            if val==1:
                S_hypothesis = list(X[0].copy())
                print("Initial : ", S_hypothesis)
                break
        for i, val in enumerate(X):
            if y[i]==1:
                count+=1
                for x in range(len(S_hypothesis)):
                    if val[x] == S_hypothesis[x]:
                        pass
                    else:
                        S_hypothesis[x] = '?'
        print("Total Positive Records : ", count)
        self.specific_hypothesis = S_hypothesis
        return S_hypothesis
    
    def predict(self, X):
        y = np.array([0 for i in range(len(X))])
        self.Xtest = X
        for i, val in enumerate(X):
            val = list(val)
            check = 0
            for x in range(len(val)):
                if val[x] == self.specific_hypothesis[x]:
                    check+=1
                else:
                    pass
            if check>0:
                y[i] = 1
            else:
                y[i] = 0
        self.ytest = y
        return y