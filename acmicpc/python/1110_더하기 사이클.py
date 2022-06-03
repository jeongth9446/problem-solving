n = int(input())
m = n
cnt = 0

while True:
    cnt += 1
    m = (m % 10 * 10) + (int(m/10) + m % 10) % 10
    if m is n:
        break

print(cnt)