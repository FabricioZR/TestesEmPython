n = float(input())

print("NOTAS:")

n100 = n//100
r1 = n%100
print("{0:.0f} nota (s) de R$ 100.00".format(n100))
n50 = r1//50
r2 = r1%50
print("{0:.0f} nota (s) de R$ 50.00".format(n50))
n20 = r2//20
r3 = r2%20
print("{0:.0f} nota (s) de R$ 20.00".format(n20))
n10 = r3//10
r4 = r3%10
print("{0:.0f} nota (s) de R$ 10.00".format(n10))
n5 = r4//5
r5 = r4%5
print("{0:.0f} nota (s) de R$ 5.00".format(n5))
n2 = r5//2
r6 = r5%2
print("{0:.0f} nota (s) de R$ 2.00".format(n2))
print("MOEDAS:")
m1 = r6//1
r7 = r6%1
print("{0:.0f} moeda (s) de R$ 1.00".format(m1))
m2 = r7//0.50
r8 = r7%0.50
print("{0:.0f} moeda (s) de R$ 0.50".format(m2))
m3 = r8//0.25
r9 = r8%0.25
print("{0:.0f} moeda (s) de R$ 0.25".format(m3))
m4 = r9//0.10
r10 = r9%0.10
print("{0:.0f} moeda (s) de R$ 0.10".format(m4))
m5 = r10//0.05
r11 = r10%0.05
print("{0:.0f} moeda (s) de R$ 0.05".format(m5))
m6 = r11//0.01
r12 = r11%0.01
print("{0:.0f} moeda (s) de R$ 0.01".format(m6))
