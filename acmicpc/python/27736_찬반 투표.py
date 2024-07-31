n = int(input())

a = list(map(int, input().split()))

approved = a.count(1)
rejected = a.count(-1)
invalid = a.count(0)

if invalid >= approved + rejected:
    print("INVALID")
elif approved > rejected:
    print("APPROVED")
else:
    print("REJECTED")
