data = input().split()
A = int(data[0])
B = int(data[1])
C = int(data[2])
N = int(data[3])
    
if C == 0:
    temp = 1
else:
    temp = pow(B, C, N)
    
result = (A * temp) % N
print(result+1)
