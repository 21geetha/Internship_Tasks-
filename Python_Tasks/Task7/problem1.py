#1.Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
result=a.symmetric_difference(b) 
print(len(result))
