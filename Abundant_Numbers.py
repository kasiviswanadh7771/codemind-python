n=int(input())
c=1
for i in range(2,n):
    if n%i==0:
        c=c+i
if c>n:
    print(True)
else:
    print(False)