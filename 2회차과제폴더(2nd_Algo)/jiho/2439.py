import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    print(" " * (n-1-i), end='')
    print("*" * (i+1))