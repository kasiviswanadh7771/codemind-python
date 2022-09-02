n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in range(n):
    if l[i]==0:
        c=c+1
for i in range(c):
    k.append(0)
for i in range(c,n):
    k.append(1)
print(*k)    