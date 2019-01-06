"""
Yossi Ben Zaken ID-315368134
"""
#-----Targil-1-----
"""
num=int(input('Enter number with 5 digits:'))
sum1=0;
if num%10%2==0:
    print(num%10,end=', ')
else:
    sum1+=num%10
num//=10
if num%10%2==0:
    print(num%10,end=', ')
else:
    sum1+=num%10
num//=10
if num%10%2==0:
    print(num%10,end=', ')
else:
    sum1+=num%10
num//=10
if num%10%2==0:
    print(num%10,end=', ')
else:
    sum1+=num%10
num//=10
if num%10%2==0:
    print(num%10,end=', ')
else:
    sum1+=num%10
print('Sum={}'.format(sum1))
"""
#Enter number with 5 digits:24685
#8, 6, 4, 2, Sum=5
#-----Targil-2-----
"""
num=float(input('Enter number 1:'))
maximum=num
num=float(input('Enter number 2:'))
if num>maximum:
    maximum=num
num=float(input('Enter number 3:'))
if num>maximum:
    maximum=num
num=float(input('Enter number 4:'))
if num>maximum:
    maximum=num
print(maximum)
"""
#Enter number 1:-6
#Enter number 2:17.7
#Enter number 3:56
#Enter number 4:-18.5
#56.0
#-----Targil-3-----
"""
num=int(input('Enter number with 4 digits:'))
f1=False
f2=False
f3=False
sum1=num%10+num//10%10+num//100%10 + num//1000
if num%10 != num//10%10 and num%10 != num//100%10 and num%10 != num//1000 and num//10%10 != num//100%10 and num//10%10 != num//1000 and num//100%10 != num//1000:
    f1=True
else:
    print('Same digit',end=', ')
    f1=False
if num%10%2 == 0 or num//10%10%2 == 0 or num//100%10%2 == 0 or num//1000%2==0:
        if num%10%2 == 1 or num//10%10%2 == 1 or num//100%10%2 == 1 or num//1000%2==1:
            f2=True
        else:
            print('No odd number',end=', ')
            f2=False
else:
    print('No even number',end=', ')
    f2=False
if 10<=sum1<=99:
    f3=True
else:
    print('Sum of digits={}'.format(sum1),end=', ')
    f3=False
if f1==True and f2==True and f3==True:
    print('Pass')
else:
    print('No Pass')
"""
#Enter number with 4 digits:1022
#Same digit, Sum of digits=5, No Pass
#-----Targil-4-----
"""
grade=int(input('Enter your grade:'))
if 0<=grade<=100:
    if grade>95:
        print('Your old grade={}, Your new grade={}'.format(grade,100))
    elif 86<=grade<=95:
        print('Your old grade={}, Factor={} , Your new grade={}'.format(grade,4,grade+4))
    elif 55<=grade<=85:
        print('Your old grade={}, Factor={} , Your new grade={}'.format(grade,6,grade+6))
    else:
        print('You fail you dont get any factor')
else:
    print('Error')
"""
#Enter your grade:70
#Your old grade=70, Factor=6 , Your new grade=76
#-----Targil-5-----
"""
height=float(input('Enter your height:'))
weight=float(input('Enter your weight:'))
BMI=weight/(height**2)
if BMI<17:
    print('Underweight')
elif 17<=BMI<=25:
    print('Healthy weight')
elif 25<BMI<=30:
    print('Overweight')
elif 30<BMI<=35:
    print('Growing fat')
elif 35<BMI<=44:
    print('Obesity')
else:
    print('Obesity is severe')
"""
#Enter your height:1.60
#Enter your weight:60
#Healthy weight
