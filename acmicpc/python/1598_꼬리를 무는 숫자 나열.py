a, b = list(map(int, input().split()))

a1, a2 = (a - 1) % 4 + 1, (a - 1) // 4
b1, b2 = (b - 1) % 4 + 1, (b - 1) // 4

print(abs(a1 - b1) + abs(a2 - b2))
