k, n = map(int, input().split())

k_arr = []

for i in range(k):
    k_arr.append(int(input()))

# print(k, n)
# print(k_arr)

k_sum = sum(k_arr)

# print(k_sum)

unit = k_sum // n

s = 0
e = unit

while(s <= e):

    m = (s+e)//2

    if m == 0:
        break
    #print(s, e, m)
    res = []
    for i in k_arr:
        res.append(i // m)
    # Rprint(sum(res))
    if(sum(res) < n):
        e = m-1
    else:
        s = m+1
print(e)