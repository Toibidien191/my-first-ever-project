import os
print('xin hãy chọn phép tính')
print(' ')
print('1: phép cộng')
print('2: phép trừ')
print('3: phép nhân')
print('4: phép chia')
sigma=float(input('>'))
os.system('cls')
print('số đầu tiên của bạn là gì?: ')
num1=float(input('>'))
os.system('cls')
print('số thứ hai của bạn là gì?: ')
num2=float(input('>'))
os.system('cls')
if sigma==1:
    print('đáp án là: ',num1+num2)
    os.system('pause')
elif sigma==2:
    print('đáp án là: ',num1-num2)
    os.system('pause')
elif sigma==3:
    print('đáp án là: ',num1*num2)
    os.system('pause')
elif sigma==4:
    print('đáp án là: ',num1/num2)
    os.system('pause')
#đm mất 1 ngày chỉ để lm cái này