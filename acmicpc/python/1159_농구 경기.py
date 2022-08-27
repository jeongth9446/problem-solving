import collections
import sys

input = sys.stdin.readline

people = collections.defaultdict(int)
n = int(input())

for _ in range(n):
    people[input()[0]] += 1

# print(people)
lst = list()
for key, value in people.items():
    if value >= 5:
        lst.append(key)

lst.sort()
if len(lst) == 0:
    print("PREDAJA")
else:
    print("".join(lst))
