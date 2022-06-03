t = int(input())

for i in range(1, t+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print("Case #" + str(i) + ": " + str(a+b))
