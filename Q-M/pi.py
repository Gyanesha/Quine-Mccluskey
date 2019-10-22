a=input().split(" ")
op=[]
for i in range(len(a)):
    op.insert(i,[[a[i]],('{0:07b}'.format(int(a[i]))),0,0,[('{0:07b}'.format(int(a[i])))]])
print(op)
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
    print(check)
    if check == 0:
        break

print(s)
ui.sort()
"""0 1 2 8 9 15 17 21 24 25 27 31"""
print(ui)
print(op)
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
ans=[]
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

print(ans)
print(chart)

