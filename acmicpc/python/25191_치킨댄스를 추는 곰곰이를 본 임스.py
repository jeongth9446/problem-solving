n = int(input())
a, b = list(map(int, input().split()))

print(min(n, a // 2 + b))