for num1 in range(10,100):
    for num2 in range(10,100):
        num3=200-num1-num2
        sum1=num1%10 + num2%10 + num3%10
        sum2=num1//10 + num2//10 + num3//10
        if 10<=num3<100 and sum1%5==0 and sum2%2==0:
            print('{} {} {} = 200'.format(num1,num2,num3))
