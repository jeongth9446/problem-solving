def hanoi(n: int, from_: int, to_: int):
    if n == 1:
        print(from_, to_)
    else:
        hanoi(n - 1, from_, 6 - from_ - to_)
        print(from_, to_)
        hanoi(n - 1, 6 - from_ - to_, to_)


n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 3)  # n개의 원판을 1번 막대에서 3번 막대로 이동
