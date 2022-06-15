import collections

n = int(input())

arr_n = list(map(int, input().split()))

dict_n = collections.defaultdict(int)

# list에서 탐색하면 시간이 오래걸리므로, dict으로 변환 후 검색 진행
for item in arr_n:
    dict_n[item] = 1

m = int(input())

arr_m = list(map(int, input().split()))

res = [ 1 if item in dict_n else 0 for item in arr_m ]

for item in res:
    print(item, "", end="")