#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    for each in range(1, len(q)+1):
        Ind = q.index(each) 
        if Ind == each-1:
            pass
        else:
            try:
                if q[each-1]+1 == q[each] or q[each-2]+1 == q[each-1]:
                    pass
            except:
                pass

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
