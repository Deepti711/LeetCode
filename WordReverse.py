#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:19:15 2018

@author: deeptichavan
"""

T = (int)(input())

while T > 0:
    T = T-1
    s = input().split(".")
    rev = s[::-1]
    rev = ".".join(rev)
    print(rev)
    
    t = "      "
    print(t.trim())