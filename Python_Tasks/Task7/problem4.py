#4.Funny String
#https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    r = s[::-1]

    for i in range(len(s) - 1):
        a = abs(ord(s[i + 1]) - ord(s[i]))
        b = abs(ord(r[i + 1]) - ord(r[i]))

        if a != b:
            return "Not Funny"

    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')

    fptr.close()
