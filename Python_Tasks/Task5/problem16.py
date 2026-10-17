#16. Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
shoes = list(map(int, input().split()))
count = Counter(shoes)

customers = int(input())
money = 0

for i in range(customers):
    size, price = map(int, input().split())

    if count[size] > 0:
        money += price
        count[size] -= 1

print(money)
