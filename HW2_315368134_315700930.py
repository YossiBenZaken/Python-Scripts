"""
Yossi Ben Zaken ID-315368134
Elinor Bendelac ID-315700930
"""
#-----Targil-1-----
'''
H=int(input('Enter hours of start:'))
M=int(input('Enter minutes of start:'))
S=int(input('Enter seconds of start:'))
FL=int(input('Enter seconds of flight time:'))
if 0<=H<24 and 0<=M<60 and 0<=S<60:
    time=FL+S+M*60+H*3600
    D,H,M,S=time//86400,time%86400//3600,time%86400%3600//60,time%86400%3600%60
    if H>0:
        print('{} hour'.format(H),end='')
        if H>1:
            print('s',end='')
        if M==0 and S==0:
            print(' exactly')
        else:
            print(end=', ')
    if M>0:
        print('{} minute'.format(M),end='')
        if M>1:
            print('s',end='')
        if S>0:
            print(end=', ')
    if S>0:
        print('{} second'.format(S),end='')
        if S>1:
            print('s',end='')
        if D>0:
            print(end=' ')
    if D>0:
        print('(+{} Day'.format(D),end='')
        if D>1:
            print('s',end='')
        print(')')
            
else:
    print('Error')
'''
#Enter hours of start:23
#Enter minutes of start:5
#Enter seconds of start:0
#Enter seconds of flight time:10
#23 hours, 5 minutes, 10 seconds
#-----Targil-2-----
'''
n=int(input('Enter number:'))
max1=n
maxsum=0
while n<10 or n > 99:
    sum1=0
    temp=n
    while temp:
        if temp%10%2==0:
            sum1+=temp%10
        temp//=10
    if sum1 > maxsum:
        maxsum=sum1
        max1=n
    n=int(input('Enter number:'))
print(max1)
'''
#Enter number:8
#Enter number:3135
#Enter number:967
#Enter number:1234321
#Enter number:125
#Enter number:989
#Enter number:271
#Enter number:894
#Enter number:15
#894
#-----Targil-3-----
'''
n1=1
n2=1
sum1=0
for x in range(1000):
    sum1=n1+n2
    n1=n2
    n2=sum1
    if 99<sum1<1000:
        print(sum1,end=' ')
'''
#144 233 377 610 987
#-----Targil-4-----
#סעיף א
'''
n=int(input('Enter number:'))
sum1=0
for x in range(1,n):
    if n%x == 0:
        sum1+=x
if sum1==n:
    print('Yes')
else:
    print('No')
'''
#Enter number:6
#Yes
#סעיף ב
'''
for x in range(0,10000):
    sum1=0
    for y in range(1,x):
        if x%y == 0:
            sum1+=y
    if sum1==x:
        print(x,end=' ')
'''
#0 6 28 496 8128
#-----Targil-5-----
'''
n=int(input('Enter odd integer number[1-19]'))
numrun=1
if n%2!=1 or n<0:
    print('Error')
else:
    for x in range(1,(n+1)//2+1):
        if x<(n+1)//2+1:
            for y in range(1,(n+1)//2-x+1):
                print("  ",end='')
            for y in range(2*x-1):
                if numrun <10:
                    print(numrun,end=' ')
                    numrun+=1
                else:
                    numrun=1
                    print(numrun,end=' ')
                    numrun+=1
        print()
    for x in range(1,(n+1)//2):
        if x<(n+1)//2+1:
            for y in range(1,x+1):
                print("  ",end='')
            for y in range(n-2*x):
                if numrun <10:
                    print(numrun,end=' ')
                    numrun+=1
                else:
                    numrun=1
                    print(numrun,end=' ')
                    numrun+=1
        print()
'''
#Enter odd integer number[1-19]11
#          1 
#        2 3 4 
#      5 6 7 8 9 
#    1 2 3 4 5 6 7 
#  8 9 1 2 3 4 5 6 7 
#8 9 1 2 3 4 5 6 7 8 9 
#  1 2 3 4 5 6 7 8 9 
#    1 2 3 4 5 6 7 
#      8 9 1 2 3 
#        4 5 6 
#          7
