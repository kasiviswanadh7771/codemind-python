n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    d=d+i
a=d/n
print(format(a,"0.2f"))
    
