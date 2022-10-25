def count(n):
    k=0
    while n>0:
       r=n%10
       k=k+1
       n=n//10
    return k
n=int(input())
l=list(map(int,input().split()))
c=0
n=[]
for i in l:
    n.append(count(i))
for i in n:
    if i==min(n):
        c=c+1
print(c)        
    