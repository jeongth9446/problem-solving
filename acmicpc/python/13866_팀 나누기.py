a, b, c, d = list(map(int, input().split()))

S = a + b + c + d
A = max(a, b, c, d) + min(a, b, c, d)
S -= A

print(abs(S - A))
