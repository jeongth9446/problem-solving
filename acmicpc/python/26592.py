n = int(input())

for _ in range(n):
    a, b = list(map(float, input().split()))

    print("The height of the triangle is", format(a*2/b, ".2f"), "units")