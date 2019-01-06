'''
Yossi Ben Zaken ID:315368134
'''
#-------Targil 1----
H=int(input("Enter hours of start:"))
M=int(input("Enter minutes of start:"))
S=int(input("Enter seconds of start:"))
FL=int(input("Enter seconds of flight time:"))
time=FL+S+M*60+H*3600
D=time//86400
H=time%86400//3600
M=time%3600//60
S=time%3600%60
print('Days = {} Hours = {} Minutes = {} Seconds = {}'.format(D,H,M,S))
