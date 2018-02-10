#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:09:55 2018

@author: deeptichavan
"""

T = (int)(input())

while T > 0:
    number = (int)(input())
    T = T - 1
    
    count = 0
    while number > 0:
        b = number & 1
        number = number >> 1
        if(b == 1):
            count += 1
    
    print(count)    