
def is_prime_number(k: int) -> bool:
    if k == 1: return False
    else:
        for i in range(2, k):
            if k % i == 0: return False

    return True


m = int(input())
n = int(input())

sum = 0
min_prime_num = 0
for item in range(m, n+1):
    if(is_prime_number(item)):
        sum += item
        if(min_prime_num == 0):
            min_prime_num = item



if(min_prime_num == 0):
    print(-1)
else:
    print(sum)
    print(min_prime_num)