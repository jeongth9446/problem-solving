br, bc = list(map(int, input().split()))
dr, dc = list(map(int, input().split()))
jr, jc = list(map(int, input().split()))

b = max(abs(br - jr), abs(bc - jc))
d = abs(dr - jr) + abs(dc - jc)

if b < d:
    print("bessie")
elif b > d:
    print("daisy")
else:
    print("tie")
