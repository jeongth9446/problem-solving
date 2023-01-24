while True:
    s = list(map(str, input().split()))
    if s[0] == "***":
        break

    n = int(input())

    k = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    kk = ["A", "Bb", "Cb", "B#", "Db", "D", "Eb", "Fb", "E#", "Gb", "G", "Ab"]
    for i in s:
        p = -1
        for idx in range(len(k)):
            if k[idx] == i:
                p = idx
                break
        if p == -1:
            for idx in range(len(kk)):
                if kk[idx] == i:
                    p = idx
                    break
        print(k[(p + n) % 12], end=" ")

    print()
