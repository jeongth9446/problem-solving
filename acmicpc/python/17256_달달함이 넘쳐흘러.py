ax, ay, az = list(map(int, input().split()))
cx, cy, cz = list(map(int, input().split()))

print(cx - az, cy // ay, cz - ax)
