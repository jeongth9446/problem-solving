n = int(input())

print("Gnomes:")
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if a < b < c or a > b > c:
        print("Ordered")
    else:
        print("Unordered")
