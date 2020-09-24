def ALG():

    A = [0,1,2,3,4,5,6,7,8,9]
    B = [10,11,12,13,14,15,16,17,18,19]
    X = int(input())

    for i in (A):
        if X == i:
            pos = A.index(i)
            break

    print (B[pos])

ALG()
