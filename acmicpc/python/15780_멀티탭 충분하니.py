n, k = list(map(int, input().split()))

A = list(map(int, input().split()))

plug = 0

for item in A:
    plug += int((item+1)/2)

if plug >= n:
    print("YES")
else:
    print("NO")