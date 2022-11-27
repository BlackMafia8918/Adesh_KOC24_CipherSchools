# Complete the 'findPoint' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy

import math
import os
import random
import re
import sys
def findPoint(px, py, qx, qy):
    if __name__ == '__main__':
        fptr = open(os.environ[Output_Path], 'w')
n = int(input().strip())

for n_itr in range(n):
    first_multiple_input = input().rstrip().split()

    px = int(first_multiple_input[0])
    py = int(first_multiple_input[1])
    qx = int(first_multiple_input[2])
    qy = int(first_multiple_input[3])

    result = findPoint(px, py, qx, qy)
    print(result)

    fptr.write()
    fptr.write(' '.join(map(str,result)))
    fptr.write('\n')
        
    fptr.close()
