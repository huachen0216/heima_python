# -*- coding: utf-8 -*-
import random

player = int(input('请出拳： 0--石头；1--剪刀；2--布；'))

computer = random.randint(0, 2)
print(f'computer is {computer}')

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('player is win! ')
elif player == computer:
    print('平局，再来一局! ')
else:
    print('computer is win! ')
