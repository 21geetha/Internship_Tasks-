#12.Making Anagrams
#https://www.hackerrank.com/challenges/making-anagrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    count = 0

    for ch in "abcdefghijklmnopqrstuvwxyz":
        count += abs(s1.count(ch) - s2.count(ch))

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
