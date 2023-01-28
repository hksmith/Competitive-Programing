#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    a = arr[n - 1]
    d = n
    while(1):
        if a < arr[n  - 2]:
            arr[n - 1] = arr[n - 2]
            print(*arr)
            if n - 2 == 0:
                arr[0] = a
                print(*arr)
                break
        else:
            arr[n - 1] = a
            print(*arr)
            break
        n -= 1
if __name__ == '__main__':
    n = int(input().strip() )

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
