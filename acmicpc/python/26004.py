import collections

a = collections.defaultdict(int)

n = int(input())

for item in list(input()):
    a[item] += 1

print(min(a['H'], a['I'], a['A'], a['R'], a['C']))
