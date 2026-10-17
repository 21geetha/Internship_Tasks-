# 10.Swap Case
# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    result=s.swapcase()
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
