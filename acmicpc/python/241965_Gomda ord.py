s = list(input())

p = 0
while p < len(s):
    print(s[p], end="")
    p += ord(s[p]) - ord('A') + 1
