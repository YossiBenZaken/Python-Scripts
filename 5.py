'''
n=5
for _ in range(n):
    print('1',end='')
print()
for i in range(n-2):
    for _ in range(n):
        print('0',end='')
    print()
for _ in range(n):
    print('9',end='')
print()
n=5
for i in range(n):
    for _ in range(n):
        if i==0:
            print('1',end='')
        elif i==n-1:
            print('9',end='')
        else:
            print('0',end='')
    print()
n=5
for i in range(n):
    for _ in range(n-(i+1)):
        print(' ',end='')
    for _ in range(i*2+1):
        print('0',end='')
    print()
'''
n=5
for i in range(n):
    for _ in range(n-(i+1)):
        print(' ',end='')
    for x in range(i+1):
        print(x+1,end='')
    for x in range(i,0,-1):
        print(x,end='')
    print()
