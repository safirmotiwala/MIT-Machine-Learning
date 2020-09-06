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
        self.ndx, self.ndy, self.ndt, self.ndp, self.ndn, self.nt_ent = "", "", "", "", "", ""
        self.unique_vals = np.unique(self.Xtrain)
        #print(self.unique_vals)
        self.nu = len(self.unique_vals)
        self.root = Node(self.nu)
        self.mstack = mystack()
        self.head = copy.copy(self.root)
        
    def add_features(self, dataset):
        for i in range(len(dataset.columns)):
            if dataset.columns[i]!='party':
                key_generator = 'f' + str(i)
                self.features[key_generator] = dataset.columns[i]
        return True
        
    def total_entropy_find(self):
        dataset = self.ytrain
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
    
    def get_subentropy(self, feature):
        print("Entropy")
        col = int(feature[1])
        unique_vals = np.unique(self.ndx[col], axis = 0)
        #print(unique_vals)
        e = []
        total_votes = []
        avg_info_entropy = 0
        for i in unique_vals:
            #e1 = self.Xtrain[:, col][np.where(self.Xtrain[:, col]==i)]
            e1 = np.where(self.ndx[:, col]==i)
            e2 = self.ndy[e1] # Fetching ytrain data with row indexes
            t = len(e2)
            p = np.count_nonzero(e2)
            n = t - p
            entropy = -(p/t)*np.log2(p/t) - (n/t)*np.log2(n/t)
            e.append([i, t, p, n, entropy])
            total_votes.append(t)
            print("Hello")
            print("TV", total_votes)
            avg_info_entropy += (t/self.total) * entropy 
        #print(e)
        return [total_votes, avg_info_entropy]
    
    def get_gain(self, features, fi):
        for fi in fi:
            features[fi] = self.total_entropy - features[fi] # Replacing avg entropy with gain
        return features
    
    def get_subgain(self, features, fi, fd):
        for fi in fi:
            if fi not in fd:
                features[fi] = self.nt_ent - features[fi] # Replacing avg entropy with gain
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
        self.root.prob1 = self.total_positive
        self.root.prob2 = self.total_negative
        # Printing Root Node
        print("Initial : ", self.root.initial)
        print("Title : ", self.root.title)
        print("Dataset : ", self.root.dataset)
        print("Entropy : ", self.root.entropy)
        print("Gain : ", self.root.gain)
        print("Total Yes's : ", self.root.yes)
        print("Total No's : ", self.root.no)
        print("Total No Votes : ", self.root.novote)
        print("Probability 1 : ", self.root.prob1)
        print("Probability 2 : ", self.root.prob2)
        return True
    
    def build_new_node(self, node_initial, cont, cont1, total_votes):
        print("New node function")
        print(total_votes)
        new_node = Node(self.nu)
        new_node.initial = node_initial
        new_node.title = self.features[node_initial]
        new_node.dataset = self.Xtrain[:, int(node_initial[1])]
        new_node.entropy = cont[node_initial]
        new_node.gain = cont1[node_initial]
        new_node.yes = total_votes[0]
        new_node.no = total_votes[1]
        new_node.novote = total_votes[2]
        new_node.prob1 = self.ndp
        new_node.prob2 = self.ndn
        # Printing Root Node
        print("Initial : ", new_node.initial)
        print("2")
        print("Title : ", new_node.title)
        print("Dataset : ", new_node.dataset)
        print("Entropy : ", new_node.entropy)
        print("Gain : ", new_node.gain)
        print("Total Yes's : ", new_node.yes)
        print("Total No's : ", new_node.no)
        print("Total No Votes : ", new_node.novote)
        print("Probability 1 : ", new_node.prob1)
        print("Probability 2 : ", new_node.prob2)
        return new_node
    
    def build_temporary_dataframe(self, feature, side, nu):
        print(feature)
        Xt, yt = self.Xtrain, self.ytrain
        col = int(feature[1])
        take_val = side
        y1 = np.where(Xt[:,col]==take_val)
        y2 = yt[y1]
        #print(y1)
        #print(y2)
        y1 = Xt[y1]
        #print(y1)
        dataset = y2
        dataset = dataset.reshape(len(dataset), 1)
        num_rows, num_columns = np.shape(dataset)[0], np.shape(dataset)[1]
        total = num_rows * num_columns
        positive = np.count_nonzero(dataset)
        negative = total - positive
        print(positive)
        print(negative)
        ent = -(positive/total)*np.log2(positive/total) - (negative/total)*np.log2(negative/total)
        print(ent)
        self.nt_ent = ent
        self.ndp, self.ndn, self.ndt = positive, negative, total
        return [y1,y2]
    
    def traverse_tree(self):
        print(self.mstack.stack)
        s = self.mstack.stack[0]
        temp = []
        while(True):
            try:
                temp.append(s[0].initial)
                s = s[1]
            except IndexError:
                break
        print("--->".join(temp))
        
    
    def decision_tree(self):
        # STEP 1 : Find Total Entropy
        self.total_entropy_find()
        feature_initials = [key for key in self.features.keys()]
        print(feature_initials)
        features_done = []
        total_votes = {}
        for fi in feature_initials:
            t = self.get_entropy(fi)
            total_votes[fi], self.container[fi] = t[0], t[1]
        print("--------------Features Average Info Entropies-------------------")
        print(self.container)
        cont = copy.deepcopy(self.container)
        self.container1 = self.get_gain(self.container, feature_initials)
        print("--------------Features Gain-------------------")
        print(self.container1)
        root = self.get_root(self.container1)
        print("Root Node : ", root)
        
        features_done.append(root)
        
        # Building Root Node
        root_creation = self.build_root(root, cont, total_votes[root])
        tn = [self.root]
        stat = self.mstack.push(tn)
        print(self.mstack.stack)
        
        
        nu = len(self.unique_vals)
        nodes_sides = [x for x in range(0, nu)]
        print(nodes_sides)
        # Building Sub Trees
        nd = self.build_temporary_dataframe(self.root.initial, nodes_sides[0], nu)
        track = self.mstack.stack[0]
        count = 0
        while(True):
            try:
                count+=1
                self.ndx = nd[0]
                self.ndy = nd[1]
                total_votes = {}
                container = {}
                for fi in feature_initials:
                    if fi not in features_done:
                        t = self.get_entropy(fi)
                        total_votes[fi], container[fi] = t[0], t[1]
                print("--------------Features Average Info Entropies-------------------")
                print(container)
                cont = copy.deepcopy(container)
                container1 = self.get_subgain(container, feature_initials, features_done)
                print("--------------Features Gain-------------------")
                print(container1)
                new_node = self.get_root(container1)
                print("New Node : ", new_node)
                node_created = self.build_new_node(new_node, cont, container1, total_votes[new_node])
                tn = [node_created]
                track.append(tn)
                track = track[1]
                #print(track[0].initial)
                features_done.append(node_created.initial)
                print(features_done)
                nd = self.build_temporary_dataframe(track[0].initial, nodes_sides[0], nu)
            except IndexError:
                break
        self.traverse_tree()
        print(features_done)
        
        
            
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
        

            