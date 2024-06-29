n, k = map(int, input().split())

a = list(map(int, input().split(",")))


for i in range(k):
    b = []
    for j in range(len(a)-1):
        b.append(a[j+1] - a[j])
    a = b

for i in range(len(a)):
    if i + 1 == len(a):
        print(str(a[i]), end="")
    else:
        print(str(a[i])+",", end="")