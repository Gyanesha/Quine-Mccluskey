import math

an=input("minterms=").split(" ")
dontcare=input("don't cares=").split(" ")
a=an
ans=[]
if len(dontcare) != 0 and dontcare[0]!= '':
    a=a+dontcare
op=[]
"""print(a)"""
for i in range(len(a)):
    op.insert(i,[[a[i]],('{0:07b}'.format(int(a[i]))),0,0,[('{0:07b}'.format(int(a[i])))]])
"""print(op)"""
l=len(op)
s=set()
ui=[]
while True:
    q=len(op)
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

                    if b.issubset(s) == False:
                        s.add(t)
                        ui=list(set(ui+list(set(op[i][0]+op[j][0]))))

                        op.append([op[i][0]+op[j][0], op[i][1][:p] + '-' + op[i][1][(p + 1):], 0,0,op[i][4]+op[j][4]])
    for j in range(len(op)-1,-1,-1):
        if op[j][2] == 1 or op[j][3] == 1 :
            op.pop(j)
    """print(check)"""
    if check == 0:
        break
for i in range(len(op)):
    if len(op[i][0]) == 1:
        ans.append(i)
print(s)
ui.sort()
if len(dontcare) != 0:
    for i in range(len(dontcare)):
        if dontcare[i] in ui:
            ui.remove(dontcare[i])

"""0 1 2 8 9 15 17 21 24 25 27 31"""

print(op)
print(dontcare)
print(ui)
chart=[]

for i in range(len(op)):
    hold=[]
    for j in range(len(ui)):
        if ui[j] in op[i][0]:
            hold.append(1)
        else:
            hold.append(0)
    chart.append(hold)

print(chart)
while True:
    while True:
        hold = []
        c = 0
        for i in range(len(chart[0])):
            t = 0
            p = 0
            for j in range(len(op)):
                t = t + chart[j][i]
                if chart[j][i]:
                    p = j

            if t == 1:
                hold.append([i, p])
                print(hold)
                c = c + 1
        for i in range(len(hold)):
            ans.append(hold[i][1])
            for k in range(len(chart[0])):
                if chart[hold[i][1]][k] == 1:
                    for j in range(len(chart)):
                        chart[j][k] = 0

        if c == 0:
            break
    print(chart)
    dominating=[]
    dominated=[]
    repeat1=[]
    repeat2=[]
    check=0
    for i in range(len(chart[0])):
        h1=[]
        yr=0
        for j in range(len(chart)):
            h1.append(chart[j][i])
            yr=yr+chart[j][i]
        if yr > 0:

            for b in range(len(chart[0])):
                h2 = []
                if b != i:
                    sum=0
                    for h in range(len(chart)):
                        h2.append(chart[h][b])
                        sum=sum+chart[h][b]
                    if sum != 0:
                        c=0
                        for h in range(len(h1)):
                            if h1[h] >= h2[h] :
                                c = c
                            else:
                                c = c + 1
                        print(h1)
                        print(h2)
                        print(c)
                        if c == 0:
                            check = check + 1
                            if h1 == h2:
                                if b not in repeat1:
                                    dominating.append(b)
                                    repeat1.append(i)
                            else:
                                dominating.append(i)
    for i in range(len(chart)):
        h1=[]
        yr=0
        for j in range(len(chart[0])):
            h1.append(chart[i][j])
            yr=yr+chart[i][j]
        if yr>0:

            for b in range(len(chart)):
                h2=[]
                if b != i:
                    sum = 0
                    for h in range(len(chart[0])):
                        h2.append(chart[b][h])
                        sum= sum + chart[b][h]
                    if sum !=0:
                        c = 0
                        for h in range(len(h1)):
                            if h1[h] <= h2[h]:
                                c = c
                            else:
                                c = c + 1

                        if c == 0 :
                            check = check + 1
                            """print(h1==h2)
                            print(b in repeat2)"""
                            if h1 == h2:
                                if b not in repeat2 :
                                    dominated.append(b)
                                    repeat2.append(i)
                            else:
                                dominated.append(i)
    dominating=list(set(dominating))
    dominated=list(set(dominated))
    print(dominating)
    print(dominated)
    print(repeat2)
    for i in range(len(dominating)):
        for k in range(len(chart)):
            chart[k][dominating[i]]=0
    for i in range(len(dominated)):
        for k in range(len(chart[0])):
            chart[dominated[i]][k]=0

    if check == 0:
        break
    print(chart)
ans=list(set(ans))
print(ans)
print(chart)
for i in range(len(ans)):
    print(op[ans[i]][1])
maximum=0
for i in range(len(a)):
    a[i]=int(a[i])
    if a[i] > maximum:
        maximum = a[i]
number_of_bits=int(math.log(maximum,2)) + 1
str = 'ABCDEFG'
fans=[]
for i in range(len(ans)):
    st=op[ans[i]][1]
    k=7-number_of_bits
    strin=''
    for j in range(number_of_bits):
        if st[k] != '-':
            strin= strin + str[j]
            if st[k] == '0':
                strin= strin + "'"
        k=k+1
    fans.append(strin)
for i in range(len(fans)):
    print(" ",fans[i],end = ' ')
    if i != len(fans)-1:
        print(end = '+')




