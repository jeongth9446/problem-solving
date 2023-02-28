st = list()

for _ in range(8):
    t = list(map(str, input().split()))
    # print(t)
    k = t[0].split(":")
    kk = int((int(k[0]) * 60 + int(k[1])) * 1000 + int(k[2]))
    # print(kk)
    st.append([kk, t[1]])

st.sort(key=lambda x: x[0])

# print(st)

red = 0
blue = 0

for i in range(8):
    if i == 0:
        if st[i][1] == 'R':
            red += 10
        else:
            blue += 10
    else:
        if st[i][1] == 'R':
            red += 10 - i - 1
        else:
            blue += 10 - i - 1

if red > blue:
    print("Red")
else:
    print("Blue")
