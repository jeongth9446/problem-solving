n = int(input())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

X.sort()
Y.sort()
flag = True

for i in range(len(X)):
    if X[i] > Y[i]:
        flag = False

if flag:
    print("DA")
else:
    print("NE")
