A, a, B, b, P = list(map(int, input().split()))

if A > B:
    A, B = B, A
    a, b = b, a

if P >= B >= b >= A >= a:
    print("Yes")
elif P >= B + A:
    print("Yes")
else:
    print("No")
