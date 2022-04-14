
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def quartiles(arr):
    # Write your code here
    arr.sort()
    size_arr = len(arr)
    if size_arr % 2 == 0: #Array size is even
        sub = math.floor(round((size_arr + 1) / 4 - 1))
        q1=(arr[sub]+arr[sub + 1]) / 2
        
        sub2 = int((size_arr + 1) / 2)
        q2=(arr[sub2 - 1]+arr[sub2]) / 2
        
        sub3 = math.floor(round(3 * (size_arr +1) / 4 - 1))
        
        q3= (arr[sub3] + arr[sub3 + 1]) / 2 -1
        

        return(int(q1), int(q2), int(q3))
    else:
        sub = int((size_arr + 1) / 4 )
        q1=(arr[sub-1]+arr[sub]) / 2
        
        q2=arr[int(size_arr / 2)] 
        
        sub3 = int(3 * (size_arr + 1) / 4 )
        q3= (arr[sub3-1]+arr[sub3])/2      
        return(int(q1), int(q2), int(q3))

if __name__ == '__main__':
    fptr = fptr = sys.stdout
    #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

