#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:31:29 2018

@author: deeptichavan
"""

#code

T = (int)(input())

while T != 0:
    
    n = (int)(input())
    arr = list(map(int,input().split(" ")))
    T = T - 1
    res = True
    for i in range(1, n):
        print(arr[i], "  ", arr[(i-1)//2])
        if(arr[i] > arr[(i-1)//2]):
            res = False
            break
        
    
    print(res)
