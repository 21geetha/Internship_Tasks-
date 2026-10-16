#6 Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n=int(input())
scores=list(map(int,input().split()))
scores=list(set(scores))
scores.sort()
print(scores[-2])

