#7.Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alpha[size-1:size-i-1:-1]
        middle = alpha[size-i-1]
        right = alpha[size-i:size]
        row = "-".join(left + middle + right)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
