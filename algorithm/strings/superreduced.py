#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    rx=re.compile(r"(\w)\1")
    s2=''
    while True:
        s2=rx.sub('',s)
        if len(s2)==len(s):break 
        s=s2
    return s or 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
