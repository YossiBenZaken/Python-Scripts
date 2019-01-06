"""
Yossi Ben Zaken ID-315368134
"""
#-----Targil-1-----
'''
def Min3(x,y,z):
    def Min2(x,y):
        if (lambda x,y:x<y)(x,y):
            return x
        return y
    return Min2(Min2(x,y),Min2(y,z))
'''
#>>> Min3(1,4,2)
#1
#>>> Min3(4,2,2)
#2
#>>> Min3(4,1,7)
#1
#-----Targil-2-----
'''
def Arrange(num):
    Digit=lambda x: x%10
    WithoutTheLastDigit=lambda x: x//10
    def isEven(n):
        if n%2==0:
            return True
        return False
    AddDigit=lambda x,y: x*10+y
    num1=0
    num2=0
    while num:
        if isEven(Digit(num))==True:
            num1=AddDigit(num1,Digit(num))
        else:
            num2=AddDigit(num2,Digit(num))
        num = WithoutTheLastDigit(num)
    while num2:
        num1 = AddDigit(num1,Digit(num2))
        num2 = WithoutTheLastDigit(num2)
    return num1
'''
#>>> Arrange(46842)
#24864
#>>> Arrange(1375)
#1375
#>>> Arrange(12547638)
#86421573
#-----Targil-3-----
'''
def PrintPyramid(n):
    def Print(tav,c):
        for _ in range(c):
            print(tav,end='')
    for i in range(n):
        Print(' ',n-i-1)
        Print('#',1)
        if i>=1 and i<n-1:
            j=i
            while j>=1:
                Print(j,1)
                j-=1
            j=2
            while j<=i:
                Print(j,1)
                j+=1
            Print('#',1)
        elif i==n-1:
            Print('#',n*2-2)
        print()
'''
#>>> PrintPyramid(7)
#       #
#      #1#
#     #212#
#    #32123#
#   #4321234#
#  #543212345#
# #############
#-----Targil-4-----
'''
def SumNum(n):
    GetNum=lambda x:x//10%10
    IsEven=lambda x:x%2
    AddNums=lambda x,y:x+y
    sum1=0
    for _ in range(n):
        num=int(input())
        if IsEven(GetNum(num))==0:
            sum1 = AddNums(sum1,num)
    return print('sum =',sum1)
'''
#>>> SumNum(10)
#123
#410
#354
#222
#978
#777
#555
#202
#111
#432
#sum = 547
#-----Targil-5-----
'''
from random import randrange as rand
points=0
min1=10
max1=100
def Game(level):
    global points
    global min1
    global max1
    x=rand(min1,max1)
    print(x)
    input('Press Enter to Start')
    print('\n'*100)
    num = int(input('Enter Number:'))
    if num == x:
        points+=level+1
        level+=1
        min1*=10
        max1*=10
        print('You have:{} point'.format(points))
        return Game(level)
    else:
        return print(points)
Game(1)
'''
#75
#Press Enter to Start
#100 times Enter
#Enter Number:75
#You have:2 point
#601
#Press Enter to Start
#100 times Enter
#Enter Number:601
#You have:5 point
#6188
#Press Enter to Start
#100 times Enter
#Enter Number:61
#5
