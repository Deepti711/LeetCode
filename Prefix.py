#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:17:50 2018

@author: deeptichavan
"""

import functools

def lcp(str1, str2):
    
    i = 1
    print(str1, "  ", str2)
    while(i <= len(str1) and i <= len(str2)):
        print("--", i, "  ", str1[-i], "  --  ", str2[-i])
        if(str1[-i] == str2[-i]):
            
            i += 1
        else:
            break
    i -= 1
    print(str1[-i:])
    return str1[-i:]
            

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    else:
        return functools.reduce(lcp, strs)


print(longestCommonPrefix(["aabb", "aabb", "aabb"]))