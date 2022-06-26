L = int(input())

S = list(map(int, input().split()))

S.append(0)
S.sort()

n = int(input())

if n in S:
    print("0")
else:
    for i in range(0, len(S) - 1):
        if S[i] < n < S[i + 1]:
            print((n - S[i]) * (S[i + 1] - n) - 1)
