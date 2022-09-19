n = int(input())

a = int(input())
b = int(input())
c = int(input())

if b * 2 == a + c:  # 등차수열
    d = b - a
    print(a + d * (n))
else: # 등비수열
    r = b / a
    print(a * int(pow(r, n)))
