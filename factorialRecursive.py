import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    
    if(n > 1): 
        return n * factorial(n - 1)
    else: 
        return n
    
    

if __name__ == '__main__':
    fptr = sys.stdout
    #open(os.environ['OUTPUT_PATH'], 'w')

    n = 11
    #int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
