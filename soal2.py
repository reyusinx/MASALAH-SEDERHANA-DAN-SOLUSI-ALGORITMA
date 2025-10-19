def fpb(a,b):
    while b:
        a, b = b, a%b
    return a

def kpk(a,b):
    return a*b // fpb(a,b)

n = int(input())
D = [int(input().strip()) for _ in range(n)]

hasil = D[0]

for i in range(1, n):
    hasil = kpk(hasil, D[i])

print (hasil)
