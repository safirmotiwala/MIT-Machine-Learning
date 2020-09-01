#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:21:10 2020

@author: safir
"""

import numpy as np
import pandas as pd
from my_tools import Node, DTLinkedList, mystack
import random
import copy

class information_gain:
    def __init__(self, X, y):
        self.features = {}
        self.total_entropy = 0
        self.total_positive, self.total_negative, self.total = 0, 0, 0
        self.Xtrain, self.ytrain = X, y
        self.container = {}
        self.container1 = {}
        self.root = Node()
        
    def add_features(self, dataset):
        for i in range(len(dataset.columns)):
            if dataset.columns[i]!='party':
                key_generator = 'f' + str(i)
                self.features[key_generator] = dataset.columns[i]
        return True
        
    def total_entropy_find(self, dataset):
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
        self.total_positive, self.total_negative, self.total = positive, negative, total
        return ent
    
    def get_entropy(self, feature):
        #print(self.features[feature])
        col = int(feature[1])
        unique_vals = np.unique(self.Xtrain[col], axis = 0)
        #print(unique_vals)
        e = []
        total_votes = []
        avg_info_entropy = 0
        for i in unique_vals:
            #e1 = self.Xtrain[:, col][np.where(self.Xtrain[:, col]==i)]
            e1 = np.where(self.Xtrain[:, col]==i)
            e2 = self.ytrain[e1] # Fetching ytrain data with row indexes
            t = len(e2)
            p = np.count_nonzero(e2)
            n = t - p
            entropy = -(p/t)*np.log2(p/t) - (n/t)*np.log2(n/t)
            e.append([i, t, p, n, entropy])
            total_votes.append(t)
            avg_info_entropy += (t/self.total) * entropy 
        #print(e)
        return [total_votes, avg_info_entropy]
    
    def get_gain(self, features, fi):
        for fi in fi:
            features[fi] = self.total_entropy - features[fi] # Replacing avg entropy with gain
        return features
    
    def get_root(self, features):
        root = list(features.values())[0]
        for i in list(features.keys()):
            if features[i]>root:
                root = features[i]
                capture_root = i
        return capture_root
    
    def build_root(self, root, cont, total_votes):
        self.root.initial = root
        self.root.title = self.features[root]
        self.root.dataset = self.Xtrain[:, int(root[1])]
        self.root.entropy = cont[root]
        self.root.gain = self.container1[root]
        self.root.yes = total_votes[0]
        self.root.no = total_votes[1]
        self.root.novote = total_votes[2]
        return True
    
    def subtree(self, node, place):
        if place=='left':
            print("Democrat")
        if place=='right':
            print("Republican")
        
    
    def decision_tree(self):
        feature_initials = [key for key in self.features.keys()]
        #print(feature_initials)
        
        for fi in feature_initials:
            t = self.get_entropy(fi)
            total_votes, self.container[fi] = t[0], t[1]
        print("--------------Features Average Info Entropies-------------------")
        print(self.container)
        cont = copy.deepcopy(self.container)
        self.container1 = self.get_gain(self.container, feature_initials)
        print("--------------Features Gain-------------------")
        print(self.container1)
        root = self.get_root(self.container1)
        print("Root Node : ", root)
        
        # Building Root Node
        root_creation = self.build_root(root, cont, total_votes)
        
        # Printing Root Node
        '''
        if root_creation:
            print(self.root.title)
            print(self.root.dataset)
            print(self.root.entropy)
            print(self.root.gain)
            print(self.root.yes)
            print(self.root.no)
            print(self.root.novote)
        '''
        
        # Building Sub Trees
            
        '''
        types = []
        count = 0
        #print(random.choice(feature_initials))
        
        while True:
            count +=1
            temp = []
            while True:
                pick_feature = random.choice(feature_initials)
                if pick_feature in temp:
                    pass
                else:
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
        '''
        

            