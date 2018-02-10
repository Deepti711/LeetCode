#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:32:37 2018

@author: deeptichavan
"""

def partition(A, start, end):
    pivot = A[end]
    pIdx = start
    
    for i in range(start, end):
        if(A[i] <= pivot):
            A[i], A[pIdx] = A[pIdx], A[i]
            pIdx += 1
        
    A[pIdx], A[end] = A[end], A[pIdx]
    return pIdx
    

def quickSort(A, start, end):
    
    if(start >= end):
        return
    else:
        p = partition(A, start, end)
        
        if(p == 3):
            return A[p]
        
        if(p > 3):
            return quickSort(A, start, p-1)
        
        return quickSort(A, p+1, end)
        
   

A = [7, 4, 9, 2, 5, 3, 1, 6, 8]
print(quickSort(A, 0, len(A)-1))