import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    z=0
    if arr==sorted(arr):
        return (0)    
    else:
        for i in range(1,len(arr)):
            x=arr[i]
            for j in range(i):
                if arr[j]>x:
                    (arr[i],arr[j])=(arr[j],arr[i])
                    z+=1
        
        return z

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
