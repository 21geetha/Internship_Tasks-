#20.Super Reduced String
#https://www.hackerrank.com/challenges/reduced-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        return "Empty String"
    else:
        return "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
