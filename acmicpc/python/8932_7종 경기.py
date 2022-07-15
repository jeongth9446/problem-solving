table = [[9.23076, 26.7, 1.835],
         [1.84523, 75, 1.348],
         [56.0211, 1.5, 1.05],
         [4.99087, 42.5, 1.81],
         [0.188807, 210, 1.41],
         [15.9803, 3.8, 1.04],
         [0.11193, 254, 1.88]]

t = int(input())

for _ in range(t):
    print(sum(list(map(int, map(lambda x, y: y[0] * pow(abs(y[1]-x), y[2]), list(map(int, input().split())), table)))))