i = int(input())
for c in range(0 , i-1):
    if ( i % c == 0 ):
        print("NAO PRIMO")
    else:
        print("PRIMO")
