#Working on rolling dice
import numpy as np
from random import randint

def rolling_dice():
        rand_num=np.random.randint(1,7,1,dtype=int)
        if rand_num==1:
            print(']'+'='*11+'[')
            print(']'+' '*11+'[')
            print(']'+' '*5+'o'+' '*5+'[')
            print(']' + ' ' * 11 + '[')
            print(']' + '=' * 11 + '[')

        if rand_num==2:
            print(']' + '=' * 11 + '[')
            print(']' + ' ' * 11 + '[')
            print(']' + ' ' * 4 + 'o' + ' '+'o'+' ' * 4 + '[')
            print(']' + ' ' * 11 + '[')
            print(']' + '=' * 11 + '[')

        if rand_num==3:
            print(']'+'='*11+'[')
            print(']' + ' ' * 5 + 'o' + ' ' * 5 + '[')
            print(']' + ' ' * 5 + 'o' + ' ' * 5 + '[')
            print(']' + ' ' * 5 + 'o' + ' ' * 5 + '[')
            print(']' + '=' * 11 + '[')

        if rand_num==4:
            print(']' + '=' * 11 + '[')
            print(']' + ' ' * 4 + 'o' + ' '+'o'+' ' * 4 + '[')
            print(']' + ' ' * 11 + '[')
            print(']' + ' ' * 4 + 'o' + ' ' + 'o' + ' ' * 4 + '[')
            print(']' + '=' * 11 + '[')

        if rand_num==5:
            print(']' + '=' * 11 + '[')
            print(']' + ' ' * 4 + 'o' + ' '+'o'+' ' * 4 + '[')
            print(']' + ' ' * 5 + 'o' + ' ' * 5 + '[')
            print(']' + ' ' * 4 + 'o' + ' ' + 'o' + ' ' * 4 + '[')
            print(']' + '=' * 11 + '[')

        if rand_num==6:
            print(']' + '=' * 11 + '[')
            print(']' + ' ' * 4 + 'o' + ' '+'o'+' ' * 4 + '[')
            print(']' + ' ' * 4 + 'o' + ' '+'o'+' ' * 4 + '[')
            print(']' + ' ' * 4 + 'o' + ' ' + 'o' + ' ' * 4 + '[')
            print(']' + '=' * 11 + '[')

while True:
    print('enter y to roll dice again ')
    letter=input()
    if letter=='y':
        rolling_dice()

    else:
        print('looks like you have not entered y')
        continue


