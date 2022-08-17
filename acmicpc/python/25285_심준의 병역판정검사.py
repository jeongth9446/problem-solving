import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    height, weight = list(map(int, input().split()))
    BMI = weight / pow(height / 100, 2)
    if height < 140.1:
        print(6)
    elif height < 146:
        print(5)
    elif height < 159:
        print(4)
    elif height < 161:
        if 16.0 <= BMI < 35.0:
            print(3)
        else:
            print(4)
    elif height < 204:
        if 20.0 <= BMI < 25:
            print(1)
        elif 18.5 <= BMI < 20 or 25.0 <= BMI < 30:
            print(2)
        elif 16.0 <= BMI < 18.5 or 30.0 <= BMI < 35.0:
            print(3)
        else:
            print(4)
    else:
        print(4)
