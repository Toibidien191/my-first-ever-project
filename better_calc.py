import os
import time as sextoy
apple = True

while apple:
    os.system('cls')
    print('xin chào:P')
    sextoy.sleep(1)
    os.system('cls')
    print('xin hãy chọn phép tính')
    print(' ')
    print('1: phép cộng')
    print('2: phép trừ')
    print('3: phép nhân')
    print('4: phép chia')
    sigma = float(input('>'))
    os.system('cls')
    print('số đầu tiên của bạn là gì?: ')
    num1 = float(input('>'))
    os.system('cls')
    print('số thứ hai của bạn là gì?: ')
    num2 = float(input('>'))
    os.system('cls')
    
    if sigma == 1:
        print('đáp án là: ', num1 + num2)
    elif sigma == 2:
        print('đáp án là: ', num1 - num2)
    elif sigma == 3:
        print('đáp án là: ', num1 * num2)
    elif sigma == 4:
        print('đáp án là: ', num1 / num2)
    else:
        print('wtf????????')
    
    os.system('pause')
    print('bạn có muốn tiếp tục sử dụng không? (có/không)')
    wannadoitagainbro = input('>')
    
    if wannadoitagainbro in ['có', '1', 'yes']:
        continue
    elif wannadoitagainbro in ['không', '0', 'no']:
        print('vậy thì tạm biệt bạn!')
        apple = False
    else:
        print('tôi sẽ coi như đó là không')
        apple = False