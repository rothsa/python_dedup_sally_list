#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    #Given a square matrix, calculate the absolute difference between #the sums of its diagonals.
    left_sum=0
    right_sum=0
    for i,a in enumerate(arr):
        left_sum=left_sum+a[i]
        right_sum=right_sum+a[-i-1]
    abs_sum=abs(left_sum-right_sum)
    #return abs_sum
    return abs_sum
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
