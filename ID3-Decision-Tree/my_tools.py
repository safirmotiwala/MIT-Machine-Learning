#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:38:42 2020

@author: safir
"""

class Node:
    def __init__(self, dataset):
        self.dataset = dataset
        self.left = None
        self.right = None

class DTLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
class mystack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        return True
    
    def pop(self):
        self.stack.pop()
        return True