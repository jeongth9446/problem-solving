n = int(input())

arr = []

for _ in range(n):
    arr.append(list(input())[0])

res = []
for i in range(ord('a'), ord('z')+1):
    if(arr.count(chr(i)) >= 5):
        res.append(chr(i))

if len(res) == 0:
    print("PREDAJA")
else:
    print("".join(res))