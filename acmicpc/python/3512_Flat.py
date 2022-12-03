n, c = map(int, input().split())

res = 0
bedroom = 0
balcony = 0

for _ in range(n):
    s, r = input().split()
    if r == 'bedroom':
        bedroom += int(s)
    elif r == 'balcony':
        balcony += int(s)
    res += int(s)

print(res)
print(bedroom)
print(c * (res - balcony / 2))
