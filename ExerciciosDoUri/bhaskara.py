A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
T = ((B**2) - (4 * A * C))
if T >= 0 and A != 0.0:
    delta = ((B**2) - (4 * A * C))
    raiz1 = (delta ** (1/2))
    X1 = (((-B) + (raiz1)) / (2*A))
    raiz2 = (delta ** (1/2))
    X2 = (((-B) - (raiz2)) / (2*A))
    print("R1 = {0:.5f}".format(X1))
    print("R2 = {0:.5f}".format(X2))

else:
    print("Impossivel calcular")
