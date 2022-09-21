s1, s2 = list(map(int, input().split()))

for _ in range(s1):
    a, b = list(map(int, input().split()))
    if a != b:
        print("Wrong Answer")
        exit(0)

for _ in range(s2):
    a, b = list(map(int, input().split()))
    if a != b:
        print("Why Wrong!!!")
        exit(0)

print("Accepted")

