def check_prime(x: int):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def main():
    n = int(input())

    k = max(n, 2)

    while True:
        a = list(str(k))
        b = list(str(k))
        b.reverse()
        if a == b:  # 팰린드롬이면?
            if check_prime(k):
                print(k)
                break
        k += 1


if __name__ == "__main__":
    main()
