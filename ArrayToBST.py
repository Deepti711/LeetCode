#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:50:41 2018

@author: deeptichavan
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def constructBST(beg, end, arr):
    
    
    if(beg > end):
        return None
    else:
        mid = (beg + end) // 2
        node = Node(arr[mid])
        node.left = constructBST(beg, mid-1, arr)
        node.right = constructBST(mid + 1, end, arr)
        
        return node  

def printBST(node):
    if(node == None):
        return None
    
    print(node.data, end = " ")
    printBST(node.left)
    printBST(node.right)
       
T = (int)(input())

while T > 0:
    T = T-1
    N = (int)(input())
    values = list(map(int, input().split()))
    
    node = constructBST(0, N-1, values)
    printBST(node)