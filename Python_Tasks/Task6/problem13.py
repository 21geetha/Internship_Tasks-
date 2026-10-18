#13. Set .union() Operation
#https://www.hackerrank.com/challenges/py-set-union/problem
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
result=a.union(b)
print(len(result))
