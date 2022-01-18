
import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
 thesum = 0
 for i in ar:
        thesum += i
 return thesum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input().strip())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
