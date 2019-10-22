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
        minterms.insert(i,(c,(m[i]),('{0:07b}'.format(int(m[i])))))


    print(minterms)
    minterms.sort()
    print(minterms)
    print(minterms[0][2])
    min1=[]
    t=0


    for i in range(len(minterms)):
        for j in range(i,len(minterms)):
            k=0
            p=0
            for l in range(7):
                if minterms[i][2][l] != minterms[j][2][l]:
                    k=k+1
                    p=l
            if k==1:
                min1.insert(t,(minterms[i][1],minterms[j][1],minterms[i][2][:p]+'-'+minterms[i][2][(p+1):]))
                t=t+1
    print(min1)
    min2=[]
    q=0

    for i in range(len(min1)):
        for j in range(i, len(min1)):
            k = 0
            p = 0
            for l in range(7):
                if min1[i][2][l] != min1[j][2][l]:
                    k = k + 1
                    p = l
            if k == 1:
                min2.insert(t, (min1[i][0], min1[j][0],min1[j][1],min1[i][1],min1[i][2][:p] + '-' + min1[i][2][(p + 1):]))
                t = t + 1
    print(min2)
