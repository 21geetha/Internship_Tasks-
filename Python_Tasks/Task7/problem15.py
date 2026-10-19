#15.Game of Thrones - I
#https://www.hackerrank.com/challenges/game-of-thrones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    odd = 0

    for value in count.values():
        if value % 2 != 0:
            odd += 1

    if odd <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
