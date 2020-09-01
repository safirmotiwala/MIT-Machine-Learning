#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:21:10 2020

@author: safir
"""

import numpy as np
from my_tools import Node, DTLinkedList, mystack
import random

class information_gain:
    def __init__(self):
        self.features = {}
        self.total_entropy = 0
        self.total_positive, self.total_negative = 0, 0
        
    def add_features(self, dataset):
        for i in range(len(dataset.columns)):
            if dataset.columns[i]!='party':
                key_generator = 'f' + str(i)
                self.features[key_generator] = dataset.columns[i]
        return True
        
    def total_entropy(self, dataset):
        dataset = dataset.iloc[:, 0].values
        dataset = dataset.reshape(len(dataset), 1)
        num_rows, num_columns = np.shape(dataset)[0], np.shape(dataset)[1]
        total = num_rows * num_columns
        positive = np.count_nonzero(dataset)
        negative = total - positive
        
        print(positive)
        print(negative)
        ent = -(positive/total)*np.log2(positive/total) - (negative/total)*np.log2(negative/total)
        print(ent)
        self.total_entropy = ent
        self.total_positive, self.total_negative = positive, negative
        return ent
    
    def decision_tree(self):
        feature_initials = [key for key in self.features.keys()]
        print(feature_initials)
        
        types = []
        count = 0
        print(random.choice(feature_initials))
        
        while True:
            count +=1
            temp = []
            while True:
                pick_feature = random.choice(feature_initials)
                #print("yo")
                if pick_feature in temp:
                    pass
                else:
                    #print("yo1")
                    temp.append(pick_feature)
                if len(temp)==16:
                    break
            if temp in types:
                pass
            elif count!=999:
                types.append(temp)
            else:
                break
        #print(types)
        

            