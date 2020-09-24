# A = float(input())
# B = float(input())
# C = float(input())
# A,B,C = float(input()).split()

A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)
lista = [A,B,C]
lista.sort(reverse = True)
A,B,C = lista

if (A >= B+C):
    print ("NAO FORMA TRIANGULO")

else:
    if (A**2 == B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if (A**2 > B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if (A**2 < B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if (A == B and B == C):
        print("TRIANGULO EQUILATERO")
    if (A == B and B != C) or (A == C and B != A) or (B == C and C != A):
        print("TRIANGULO ISOSCELES")

"""else:
    B = c
    C = b
elif(b >= a and b >= c):
  A = b
if (a > c):
  B = a C = c
else:
    B = c C = a
elif (c >= a and c >= b):
    A = c
if (b >= a):
    B = b C = a
else:
    B = a C = b
if(A >= B + C):
    print("NAO FORMA TRIANGULO")
else:
 if(A2) == (B2) + (C2):
  print("TRIANGULO RETANGULO")
 if(A2) > (B2) + (C2):
  print("TRIANGULO OBTUSANGULO")
if(A2) < (B2) + (C**2):
  print("TRIANGULO ACUTANGULO") if(A == B == C):
  print("TRIANGULO EQUILATERO")
elif(A == B) or (A == C) or (B == C):
  print("TRIANGULO ISOSCELES")"""
