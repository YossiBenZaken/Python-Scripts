# --------------------------------------
#   Q1
# --------------------------------------
'''
def f1(x,n):
    for _ in range(n):
        x = f2(x)
    return x
def f2(x):
    temp = x//10
    temp2 = x%10
    while x//10:
        temp2*=10
        x//=10
    return temp+temp2
x = int(input("Enter Number:"))
print(f1(x,2))
'''
def f(x):
    def f1(x1):
        if x1<=0:
            return True
        return False
    def f2(x2,x3):
        return x2+x3
    sum1,count,odd=0,0,1
    while f1(sum1+odd-x):
        sum1=f2(sum1,odd)
        odd=f2(odd,2)
        count=f2(count,1)
    return count
