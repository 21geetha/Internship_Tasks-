#19.Weighted Uniform Strings
#https://www.hackerrank.com/challenges/weighted-uniform-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    current = 0
    previous = ""

    for ch in s:
        if ch == previous:
            current += ord(ch) - ord('a') + 1
        else:
            current = ord(ch) - ord('a') + 1
            previous = ch

        weights.add(current)

    result = []

    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
