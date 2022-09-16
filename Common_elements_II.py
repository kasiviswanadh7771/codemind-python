m,n=map(int,input().split())
k=list(map(int,input().split()))
j=list(map(int,input().split()))
lst=[]
for i in k:
    if i not in j:
        lst.append(i)
for i in j:
     if i not in k:
        lst.append(i)
print(*lst)        
        