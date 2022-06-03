dic = dict()

for i in range(0, 10):
    dic[int(input()) % 42] = True

print(len(dic))
