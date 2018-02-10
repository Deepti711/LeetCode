#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:48:46 2018

@author: deeptichavan
"""

#code
import math

T = (int)(input())

while T > 0:
    T = T - 1
    
    X, Y, N = map(int,input().split())    
    hts = list(map(int,input().split()))
    jumps = 0
    for i in range(0, N):
        climb = hts[i]
        #print(climb)
        while(climb > 0):
                
            if(climb <= X):
                jumps += 1
                climb = 0
            else:
            
                climb = climb - (X - Y)
                #print(climb)
                jumps += 1
    
            #print("----", jumps)
    print(jumps)
        
    

