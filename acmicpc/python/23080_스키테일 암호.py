k = int(input())
s = list(input())

for i in range(0, len(s), k):
    print(s[i], end="")
