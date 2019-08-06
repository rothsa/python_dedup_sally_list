#!/bin/python3

import os
import sys
ar = [3,4,3,2,3]
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    print(ar)
    b = 0
    for a in ar:
        print(a)
        b+=a
    return b
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

