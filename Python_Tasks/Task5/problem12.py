# 12. Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
import os

def solve(s):
    result = ""
    capitalize_next = True

    for char in s:
        if char == ' ':
            result += char
            capitalize_next = True
        elif capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        else:
            result += char
            capitalize_next = False
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
