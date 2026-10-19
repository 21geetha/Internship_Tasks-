#2.The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
k=int(input())
rooms=list(map(int,input().split()))
captain=(sum(set(rooms))*k-sum(rooms))//(k - 1)
print(captain)
