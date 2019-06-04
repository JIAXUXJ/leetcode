#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
# ======================================MY SOLUTION START===========================================
def diagonalDifference(arr):
    n = len(arr) 
    leftVal = 0
    rightVal = 0
    for i in range(n): 
        for j in range(n): 
            # left digonal condition
            if (i == j): 
                leftVal += arr[i][j]
            # light digonal condition
            if(i + j + 1 == n):
                rightVal += arr[i][j]
                print(arr[i][j])
                
    return abs(leftVal - rightVal)
# ======================================MY SOLUTION END===========================================
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

