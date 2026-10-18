#5.Write a Function
# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap=False
    if not(year%100==0):
       return leap
    else:
        return True

year = int(input())
print(is_leap(year))
