#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    x=len(s)/3
    x=int(x)
    count=0
    y="SOS" *x
    for i in range(len(s)):
        if(s[i]!=y[i]):
            count=count+1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
