m=int(input())
for i in range(m):
    n=int(input())
    l=0
    f=0
    while n>0:
        d=n%10
        k=d*2**(l)
        f=f+k
        l=l+1
        n=n//10
    print(f)