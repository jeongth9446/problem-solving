n = int(input())

for _ in range(n):
    w, k = list(map(int, input().split()))
    print(max(w // 2 * k, w * k // 2))
