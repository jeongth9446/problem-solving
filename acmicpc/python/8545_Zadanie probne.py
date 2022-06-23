import sys

s = list(map(str, sys.stdin.readline().strip()))

s.reverse()
print("".join(s))