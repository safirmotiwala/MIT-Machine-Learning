#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:21:10 2020

@author: safir
"""

import numpy as np

class information_gain:
    def __init__(self):
        self.stack = []
        self.features = {}
        self.total_entropy = 0
        
    def add_features(self, dataset):
        for i in range(len(dataset.columns)):
            if dataset.columns[i]!='party':
                key_generator = 'f' + str(i)
                self.features[key_generator] = dataset.columns[i]
        return True
    
    def push(self, data):
        self.stack.append(data)
        return True
    
    def pop(self):
        self.stack.pop()
        
    def entropy(self, dataset):
        num_rows, num_columns = np.shape(dataset)[0], np.shape(dataset)[1]
        total = num_rows * num_columns
        positive = np.count_nonzero(dataset)
        negative = total - positive
        
        print(positive)
        print(negative)
        ent = -(positive/total)*np.log2(positive/total) - (negative/total)*np.log2(negative/total)
        print(ent)
        return ent
    
                
            