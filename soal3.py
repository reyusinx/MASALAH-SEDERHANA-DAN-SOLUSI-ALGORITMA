t = int(input().strip())

for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    tim = data[1:1+n]

    # jumlahPertandingan
    jp = n * (n - 1) // 2

    batasMin = jp * 2
    batasMax = jp * 3

    #total points
    tp = sum(tim)

    if tp < batasMin or tp > batasMax:
        print("NO")
        continue
    
    
    possible = True
    for i in tim:
        if i > 3 * (n - 1):
            possible = False
            break
    
    print("YES" if possible else "NO")

    
