pi=[]
n=int(input())
t=0
for i in range(n):
    a=set()
    l=(input().split(" "))
    a.update(l)
    pi.insert(t,a)
    t=t+1
print(pi)
sh=[]
t=0
for i in range(len(pi)):
    s=pi[i]
    k=set()
    k=s
    for j in range(len(pi)):
        if(pi[i]!= pi[j] ):
            k=k.difference(pi[j])
    if(len(k)!=0):
        sh.insert(t,pi[i])

        t=t+1
print(pi)
print(sh)
print(t)