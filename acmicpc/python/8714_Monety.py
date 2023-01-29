n = int(input())

s = list(map(int, input().split()))

print(min(s.count(1), s.count(0)))