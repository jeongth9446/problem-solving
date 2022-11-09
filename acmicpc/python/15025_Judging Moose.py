odd_even = ["Even", "Odd"]

l, r = list(map(int, input().split()))

if l != r:
    oe = 1
else:
    oe = 0

if l == r == 0:
    print("Not a moose")
else:
    print(odd_even[oe], str(max(l, r) * 2))
