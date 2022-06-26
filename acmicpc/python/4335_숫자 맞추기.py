import sys

input = sys.stdin.readline

larger = list()
smaller = list()

while True:
    t = int(input())
    if t == 0:
        break
    s = input().strip()
    if s == 'too high':
        larger.append(t)
    elif s == 'too low':
        smaller.append(t)
    else:
        flag = True
        while len(larger) > 0:
            k = larger.pop()
            if k <= t:
                flag = False
        while len(smaller) > 0:
            k = smaller.pop()
            if k >= t:
                flag = False

        if flag:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        larger = list()
        smaller = list()