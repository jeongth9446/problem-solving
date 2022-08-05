S1, S2 = list(map(int, input().split()))
N1, N2 = list(map(int, input().split()))
U1, U2 = list(map(int, input().split()))

if S1 * 10 >= 5000:
    S = S1 * 10 - 500
else:
    S = S1 * 10

if N1 * 10 >= 5000:
    N = N1 * 10 - 500
else:
    N = N1 * 10

if U1 * 10 >= 5000:
    U = U1 * 10 - 500
else:
    U = U1 * 10

S = S2 * 10 / S
N = N2 * 10 / N
U = U2 * 10 / U

if max(S, N, U) == S:
    print("S")
elif max(S, N, U) == N:
    print("N")
elif max(S, N, U) == U:
    print("U")
