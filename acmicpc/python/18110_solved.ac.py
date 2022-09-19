import sys


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


input = sys.stdin.readline
n = int(input())
score = list()

if n == 0:
    print(0)
else:
    for _ in range(n):
        score.append(int(input()))

    score.sort()
    cutoff = round2(n * 0.15)
    print(round2(sum(score[cutoff:n - cutoff]) / (n - cutoff * 2)))
