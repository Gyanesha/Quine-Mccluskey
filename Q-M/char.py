a=input().split(" ")
op=[]
for i in range(len(a)):
    op.insert(i,[[a[i]],('{0:07b}'.format(int(a[i]))),0,0,[('{0:07b}'.format(int(a[i])))]])
print(op)
l=len(op)
s=set()
while True:
    q=len(op)
    print(q)
    check=0
    for i in range(q):
        h = op[i]
        if op[i][2] == 0:
            for j in range(i, q):
                n = 0
                p = 0
                for k in range(7):
                    if op[i][1][k] != op[j][1][k]:
                        n = n + 1
                        p = k
                if n == 1:
                    t=op[i][1][:p] + '-' + op[j][1][(p + 1):]
                    b=set([t])
                    op[i][2] = 1
                    op[j][3] = 1
                    check = check + 1
                    print(check)
                    print(b)
                    if b.issubset(s) == False:
                        s.add(t)
                        op.append([op[i][0]+op[j][0], op[i][1][:p] + '-' + op[i][1][(p + 1):], 0,0,op[i][4]+op[j][4]])
    for j in range(len(op)-1,-1,-1):
        if op[j][2] == 1 or op[j][3] == 1 :
            op.pop(j)
    print(check)
    if check == 0:
        break

print(s)
"""0 1 2 8 9 15 17 21 24 25 27 31"""

print(op)



