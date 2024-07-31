t = int(input())

for i in range(t):
    n = int(input())
    print("Case #"+str(i+1)+": ", end="")
    if(n > 4500):
        print("Round 1")
    elif(n > 1000):
        print("Round 2")
    elif(n > 25):
        print("Round 3")
    else:
        print("World Finals")
