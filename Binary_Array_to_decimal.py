n=int(input())
l=list(map(int,input().split()))
m=len(l)
j=0
for i in l:
    k=(2**(m-1))*i
    m=m-1
    j=j+k
print(j)    
    