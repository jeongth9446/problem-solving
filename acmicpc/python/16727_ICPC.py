p1, s1 = list(map(int, input().split())) # 페르세폴리스 홈
s2, p2 = list(map(int, input().split())) # 에스테그랄 홈

s3 = s1 + s2
p3 = p1 + p2

if s3 > p3:
    print("Esteghlal")
elif s3 < p3:
    print("Persepolis")
else:
    f1 = 0
    f2 = 0
    if s1 > p2:
        f1 = 1
    if s1 < p2:
        f2 = 2

    if f1 == f2:
        print("Penalty")
    elif f1 == 1:
        print("Esteghlal")
    else:
        print("Persepolis")
