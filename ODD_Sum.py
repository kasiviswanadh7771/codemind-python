n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i%2==1:
        c=c+i
print(c)        
        