"""X = int(input())
if X >= 3600:
    A = int(X/3600) #horas
    A1 = X%3600 #sobra das horas
else:
    A = 0
if X >= 3600:
    B = int(X/60) #minutos
    B1 = int(X%60) #sobra dos minutos
else:
    B = 0
print(A,":",B,":",B1)
"""
X = int(input())
H = int(X/3600)
R = int(X%3600)
M = int(R/60)
S = int(R%60)
print (str(H)+":"+str(M),":",str(S))
