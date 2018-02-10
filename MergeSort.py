#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:15:46 2018

@author: deeptichavan
"""

def combine(A, start, mid, end):
    
    
    T = [0] * len(A)
    for i in range(start,end+1):
        T[i] = A[i]
        
    i = start
    j = mid + 1
    k = start
    
    
    while(i <= mid and j <= end):
        if(T[i] <= T[j]):
            A[k] = T[i]
            i += 1
        else:
            A[k] = T[j]
            j += 1
        k += 1
            
    
    while(i <= mid):
        A[k] = T[i]
        k += 1
        i +=1
        
    while(j <= end):
        A[k] = T[j]
        k += 1
        j += 1
    
    

def mergeSort(A, start, end):
    if(start >= end):
        return
    mid = (start + end)// 2
    mergeSort(A, start, mid)
    mergeSort(A, mid+1, end)
    combine(A, start, mid, end)
    return A

A = [7, 4, 9, 2, 5, 3, 1, 6, 8]
print(mergeSort(A, 0, len(A)-1))