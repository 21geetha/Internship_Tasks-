#20.Validating the Phone Number
#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
import re
n=int(input())
for i in range(n):
    number=input()
    if re.match(r'^[789][0-9]{9}$',number):
        print("YES")
    else:
        print("NO")
