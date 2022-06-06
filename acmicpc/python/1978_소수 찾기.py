
def is_prime_number(k: int) -> bool:
    if k == 1: return False
    else:
        for i in range(2, k):
            if k % i == 0: return False

    return True


n = int(input())

in_arr = map(int, input().split())
cnt = 0
for item in in_arr:
    if(is_prime_number(item)):
        cnt += 1

print(cnt)