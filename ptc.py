import math
import os
import random
import re
import sys
# Complete the 'closestNumbers' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
def closestNumbers(arr):
    # Write your code here
    arr.sort()
    ar = []
    dif = 10**7 + 1
    for i in range(len(arr)-1):
        a = arr[i:i+2]
        minm = a[1] - a[0]
        if(minm <= dif):
            if(minm < dif):
                ar = []
            dif = minm
            ar.append(a[0])
            ar.append(a[1])
    return ar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()