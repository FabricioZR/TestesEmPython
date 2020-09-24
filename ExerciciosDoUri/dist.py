x1,y1 = input().split()
x1=float(x1)
y1=float(y1)
x2,y2 = input().split()
x2=float(x2)
y2=float(y2)
so=(x2-x1)**2
ma=(y2-y1)**2
soma=(so+ma)
print("{0:.4f}".format(soma**0.5))
