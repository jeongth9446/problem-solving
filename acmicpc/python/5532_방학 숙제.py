L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C == 0:
    AA = A // C
else:
    AA = (A // C) + 1
if B % D == 0:
    BB = B // D
else:
    BB = (B // D) + 1
print(L - max(AA, BB))
