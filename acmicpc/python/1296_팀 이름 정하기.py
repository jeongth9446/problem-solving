n = list(input())

L = O = V = E = 0

for item in n:
    if item == "L":
        L += 1
    elif item == "O":
        O += 1
    elif item == "V":
        V += 1
    elif item == "E":
        E += 1

res = list()
resi = 0
n = int(input())

for _ in range(n):
    Lk = L
    Ok = O
    Vk = V
    Ek = E

    k = list(input())

    for item in k:
        if item == "L":
            Lk += 1
        elif item == "O":
            Ok += 1
        elif item == "V":
            Vk += 1
        elif item == "E":
            Ek += 1

    p = ((Lk+Ok) * (Lk+Vk) * (Lk+Ek) * (Ok+Vk) * (Ok+Ek) * (Vk+Ek)) % 100

    if p > resi:
        resi = p
        res = k
    elif p == resi:
        if len(res) == 0:
            resi = p
            res = k
        if "".join(res) > "".join(k):
            resi = p
            res = k

print("".join(res))
