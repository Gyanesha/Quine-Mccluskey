n= int(input())
k=1
while(n>k):
    if(k & n):
        n=n-k
    k=k*4
print(n)