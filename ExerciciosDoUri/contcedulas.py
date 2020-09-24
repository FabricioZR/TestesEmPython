NOTA = float(input())
A = int(NOTA/100)#qts notas de 100
Ar = NOTA%100#oq sobra de 100
B = int(Ar/50)#troco em nts de 50
Br = Ar%50#oq sobra de 50
C = int(Br/20)
Cr = Br%20
D = int(Cr/10)
Dr = Cr%10
E = int(Dr/5)
Er = Dr%5
F = int(Er/2)
Fr =Er%2
G = int(Fr)
print(NOTA)
print(A, "nota(s) de R$ 100,00")
print(B, "nota(s) de R$ 50,00")
print(C, "nota(s) de R$ 20,00")
print(D, "nota(s) de R$ 10,00")
print(E, "nota(s) de R$ 5,00")
print(F, "nota(s) de R$ 2,00")
print(G, "nota(s) de R$ 1,00")
