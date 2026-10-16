#15 Word Order
# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
n = int(input())
words = OrderedDict()
for _ in range(n):
    word = input().strip()
    words[word] = words.get(word, 0) + 1
print(len(words))
print(*words.values())
