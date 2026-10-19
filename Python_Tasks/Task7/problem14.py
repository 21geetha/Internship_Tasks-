#14.Anagram
#https://www.hackerrank.com/challenges/anagram/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2
    s1 = s[:half]
    s2 = s[half:]

    count = 0

    for ch in s1:
        if ch in s2:
            s2 = s2.replace(ch, "", 1)
        else:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
