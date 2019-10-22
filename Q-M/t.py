print("enter the minterms")
minterms =input().split(" ")
for i in range(len(minterms)):
    a=int(minterms[i])
    k=format(a, 'b')
    print(k)
    c=0
    n=int(k)
    """print(k)"""
    while (n>0):
        """print(" ",+n)"""
        if n%10 == 1:
            c=c+1
        else:
            c=c

        n=int(n/10)
    print(c)
