#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    i = 0
    x = 0
    l = len(a)
    while i < l:
        j = 0
        while j < l - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                x += 1
            j += 1
        i += 1
    print("Array is sorted in", x ,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[l - 1])
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
