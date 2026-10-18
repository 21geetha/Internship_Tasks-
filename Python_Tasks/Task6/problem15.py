#15.Set .difference() Operation
#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
result=a.difference(b) 
print(len(result))
