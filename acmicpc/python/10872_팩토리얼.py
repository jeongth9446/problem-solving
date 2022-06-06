def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n-1) * n


m = int(input())

print(factorial(m))