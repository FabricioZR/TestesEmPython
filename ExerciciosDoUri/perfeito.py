X = int(input())
A = 0
for i in range(0,X):
    Y = int(input())
    for K in range (1,Y+1):
        if Y%K == 0:
            A += K
    if A==Y:
        print(Y,"eh perfeito")
