#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
"""
input
2
5
2 1 5 3 4
5
2 5 1 3 4
"""

def minimumBribes(q):
    ft = [0] * (len(q) + 1) 
    maxn = len(ft)
    
    def lsb(i:int) -> int:
        return i & (-i)
    
    def get_ft(index:int) -> int:
        i, result = index, 0
        while i > 0:
            result += ft[i]
            i -= lsb(i)
        return result
    
    def set_ft(index:int, value:int) -> int:
        i = index
        while i < maxn:
            ft[i] += value
            i += lsb(i)
            
    result = 0
    q = [0] + q
    for i in range(len(q) - 1, 0, -1):
        ans = get_ft(q[i])
        if ans > 2:
            print("Too chaotic")
            return
        result += ans
        set_ft(q[i], 1)
    
    print(result)
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

