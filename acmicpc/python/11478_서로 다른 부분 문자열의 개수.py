import sys

S = sys.stdin.readline().strip()
set_S = set()

for i in range(len(S)):
    for j in range(len(S)+1):
        if i < j:
            set_S.add(S[i:j])
print(len(set_S))
