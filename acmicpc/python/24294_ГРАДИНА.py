w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

res = (w1 + h1 + w2 + h2 + 4) * 2 - (min(w1, w2) + 2) * 2
print(res)
