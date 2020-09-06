#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:38:42 2020

@author: safir
"""

class Node:
    def __init__(self, n):
        self.initial = ""
        self.title = ""
        self.dataset = []
        self.entropy = 0
        self.gain = 0
        self.yes = 0
        self.no = 0
        self.novote = 0
        self.prob1 = 0
        self.prob2 = 0

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