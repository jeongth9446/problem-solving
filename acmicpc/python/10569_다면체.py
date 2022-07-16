t = int(input())

for _ in range(t):
    V, E = list(map(int, input().split()))

    print(2 - V + E)
