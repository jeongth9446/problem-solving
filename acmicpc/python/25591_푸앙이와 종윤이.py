n, m = list(map(int, input().split()))

print(100 - n, 100 - m, 100 - (100 - n + 100 - m), (100 - n) * (100 - m), (100 - n) * (100 - m) // 100,
      (100 - n) * (100 - m) % 100)

print(100 - (100 - n + 100 - m) + (100 - n) * (100 - m) // 100, (100 - n) * (100 - m) % 100)
