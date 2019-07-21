#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    # iterate through comparison
    for i, a_single in enumerate(a):
    #If , then Alice is awarded  point.
        if a_single > b[i]:
            a_score+=1
    #If , then Bob is awarded  point.
        elif a_single < b[i]:
            b_score+=1
    #If , then neither person receives a point.
    return [a_score, b_score]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

