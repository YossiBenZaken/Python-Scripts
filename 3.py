'''
def f4(n):
    sum1=0
    while n:
        sum1+=n%10
        n//=10
    return sum1
def f5(n):
    sum1=n%10*10
    while n>9:
        n//=10
    return sum1+n
'''
def f6(n):
    while n>9:
        sum1=0
        while n:
            sum1+=n%10
            n//=10
        n=sum1
    return n
