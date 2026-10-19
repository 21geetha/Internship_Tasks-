#13.Sherlock and the Valid String
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def isValid(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    counts = list(freq.values())
    unique = set(counts)

    if len(unique) == 1:
        return "YES"

    if len(unique) == 2:
        a, b = sorted(unique)

        if counts.count(a) == 1 and a == 1:
            return "YES"

        if counts.count(b) == 1 and b - a == 1:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
