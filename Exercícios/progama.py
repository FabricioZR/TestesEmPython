
def fact(n):
  f = 1
  for i in range(0,n):
    f=f*(n-i)
  return f

def combinacao(n, p):
  return fact(n) / (fact(p) * fact(n-p))

def dist_binomial(n, x, p):
  return (combinacao(n, x)) * (p**x) * ((1-p)**(n-x))

print()
print("  Ola, este programa ira resolver questoes referentes a Distribuiçoes Binomiais, seja ela acumulada ou nao!  ")
print("  DISTRIBUIÇÂO BINOMINAL (digite 1)")
print("  DISTRIBUÇÂO BINOMINAL ACUMULADA (digite 2)")
print()

while True:
  user = input('  "1" ou "2": ')

  if user == "1":
    print(round(dist_binomial(int(input("  Digite o valor de N: ")), int(input("  Digite o valor de X: ")), float(input("  Digite o valor de P(Por favor, use o ponto '(x.x)': "))), 4 ))
    print()
    break

  if user == "2":
    n = int(input("  Digite o valor de N: "))
    x = int(input("  Digite o valor de  X: "))
    p = float(input("  Digite o valor de P (Por favor, use ponto e nao virgula'(x.x)': "))
    soma = 0
    for i in range(x+1):
      soma += dist_binomial(n, i, p)
    print()
    print("  Resultado = ", round(soma, 4))
    print()
    break
