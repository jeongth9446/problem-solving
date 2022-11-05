# 2810_컵홀더

n = int(input())
k = list(input())

s = k.count("S")
l = k.count("L")

star = 1 + s + (l // 2)

print(min(n, star))
