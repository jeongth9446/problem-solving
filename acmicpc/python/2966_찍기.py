n = int(input())

a = list(input())

x = ['A', 'B', 'C']
y = ['B', 'A', 'B', 'C']
z = ['C', 'C', 'A', 'A', 'B', 'B']

xscore = 0
yscore = 0
zscore = 0
for i in range(len(a)):
    if a[i] == x[i%len(x)]:
        xscore +=1
    if a[i] == y[i%len(y)]:
        yscore +=1
    if a[i] == z[i%len(z)]:
        zscore +=1

maxScore = max(xscore, max(yscore, zscore))
#print(xscore, yscore, zscore)
print(maxScore)

if maxScore == xscore:
    print("Adrian")
if maxScore == yscore:
    print("Bruno")
if maxScore == zscore:
    print("Goran")