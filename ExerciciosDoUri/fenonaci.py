n = int(input())
print(0,1,end=" ")
a=0
b=1
i=2
while i<n:
    val=a+b
    if i+1==n:
        print(val)
    else:
        print(val,end=" ")
    a=b
    b=val
    i+=1
