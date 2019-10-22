class ac:
    m=(input().split(" "))
    minterms=[]

    for i in range(len(m)):
        n=int(format(int(m[i]),'b'))
        c=0
        while(n>0):
            if n%10 == 1:
                c=c+1
            else:
                c=c
            n=int(n/10)
        minterms.insert(i,(c,int(m[i]),int(format(int(m[i]),'b'))))


    print(minterms)
    minterms.sort()
    print(minterms)
    mins=[]
    k=1
    j=minterms[0][0]
    for i in range(len(minterms)):
        if (j == minterms[i][0]):
            mins.insert(k,(minterms[i][1],minterms[i][2]))
        else:
            k=k+1
            j=minterms[i][0]
            mins.insert(k, (minterms[i][1], minterms[i][2]))
    print(mins)
    print(len(mins))
    print(mins[0][1])
    print(mins[3][0])
    """print(mins[2][2])"""