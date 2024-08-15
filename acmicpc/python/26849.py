n = int(input())
max_ = 0
min_ = 100000000000
sum_ = 0
for _ in range(n):
    a, b = list(map(float, input().split()))
    min_ = min(min_, a/b)
    max_ = max(max_, a/b)
    sum_ = sum_ + a/b
print(min_, max_, sum_)