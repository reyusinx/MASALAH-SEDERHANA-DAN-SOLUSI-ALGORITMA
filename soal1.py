n = int(input())

baju = [int(input().strip()) for _ in range(n)]

if n % 2 != 0:
    t = n//2
    print(baju[t]/1)
else:
    tengah1 = n//2
    tengah2 = tengah1-1
    fixTengah = (baju[tengah1]+baju[tengah2])/2
    print(fixTengah)
