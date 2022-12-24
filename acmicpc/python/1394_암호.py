chk = [0 for i in range(200)]

p = list(input())
cnt = 0
for item in p:
    cnt += 1
    chk[ord(item)] = cnt

data = list(input())
data_n = len(data)

g = 1

res = 0
for i in range(0, data_n):
    k = data_n - i - 1
    res = (res + g * chk[ord(data[k])]) % 900528
    g = g * cnt % 900528

print(res)
