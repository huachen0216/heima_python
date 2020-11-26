# -*- coding: utf-8 -*-

age = int(input('age: '))

if age < 18:
    print(f'{age}不合法')
elif age > 60:
    print(f'{age}退休')
elif 18 <= age <= 60:
    print(f'{age}合法工作')

