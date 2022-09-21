while True:
    n = float(input())
    if n == -1:
        break
    print("Objects weighing {0:0.2f} on Earth will weigh {1:0.2f} on the moon.".format(n, n * 0.167))
