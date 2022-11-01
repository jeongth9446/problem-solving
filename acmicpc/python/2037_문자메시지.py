def latency(v: str):
    mapping = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]
    return mapping[ord(v) - ord('A')]


def same_group(v: str, u: str):
    mapping = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7]
    # print(v, u)
    if v == ' ' or u == ' ':
        return False
    else:
        return mapping[ord(v) - ord('A')] == mapping[ord(u) - ord('A')]


p, w = list(map(int, input().split()))

message = list(input())

res = 0

pre_item = ''
for item in message:
    if pre_item == '':  # start position
        res += latency(item) * p
    elif item == ' ':  # space
        res += p
    else:
        if same_group(item, pre_item):
            res += w + latency(item) * p
        else:
            res += latency(item) * p
    pre_item = item

print(res)
