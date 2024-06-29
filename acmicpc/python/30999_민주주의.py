n, m = map(int, input().split())

res = 0
for i in range(n):
    k = list(input())
    if(k.count("O") * 2 > m):
        res += 1

print(res)