a1, b1, a2, b2 = list(map(int, input().split()))
c1, d1, c2, d2 = list(map(int, input().split()))

resa = resb = 0
for a in range(a1, b1 + 1):
    for b in range(a2, b2 + 1):
        for c in range(c1, d1 + 1):
            for d in range(c2, d2 + 1):
                if a + b > c + d:
                    resa += 1
                elif a + b < c + d:
                    resb += 1

if resa > resb:
    print("Gunnar")
elif resa < resb:
    print("Emma")
else:
    print("Tie")
