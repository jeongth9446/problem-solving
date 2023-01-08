n = int(input())

resa = min(n + 8, 210)
resb = min(n + 4, 220)
resc = min(n + 2, 230)
resd = min(n + 1, 240)

res = 0
if max(resa, resb, resc, resd) == resa:
    res = 1
if max(resa, resb, resc, resd) == resb:
    res = 2
if max(resa, resb, resc, resd) == resc:
    res = 3
if max(resa, resb, resc, resd) == resd:
    res = 4

print(res)
