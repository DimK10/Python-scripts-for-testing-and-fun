# This code was created by Mohammad Hashem
import os
import time
import random
import string
from random import randint
from colorama import init, Fore, Back, Style

init(convert=True)

os.system("C:\\Python34\\valentine\\music_Val.bat")

for i in range(1,45):
    print('')
play = 0
while play == 0:
    Left_Spaces = randint(8, 80)
    Loves = 8
    for i in range(1,17):
        count = Left_Spaces
        while count > 0:
            print(' ', end='')
            count -= 1
        count = Loves
        while count > 0:
            if i == 1 and count == 4:
                print('    ', end='')
            elif i < 3 and count == 5:
                print('    ', end='')
            else:
                print(Fore.RED + Style.BRIGHT + 'LOVE', end='')
            count -= 1

        if i < 5:
            Left_Spaces = Left_Spaces - 2
            Loves += 1
        else:
            Left_Spaces = Left_Spaces + 2
            Loves -= 1

        time.sleep(0.3)
        print('\n', end='')

    print('\n', end='')
    time.sleep(0.3)
    count = randint(8, 80)

    while count > 0:
        print(' ', end='')
        count -= 1
    print(Fore.MAGENTA + Style.BRIGHT + 'H a p p y  V a l e n t i n e ! ! !')
    time.sleep(0.3)
    print('\n', end='')
    time.sleep(0.3) # By Mohammad Hashem
