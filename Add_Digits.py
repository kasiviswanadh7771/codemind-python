def num(n):
    while n>0:
        r=n%10
        c=n//10
        n=r+c
        if n<9:
            return n
a=int(input())
print(num(a))