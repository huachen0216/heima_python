# -*- coding: utf-8 -*-

i = 1

while i <= 5:
    if (i == 3):
        print(f'第{i}苹果坏了。')
        i += 1
        continue
    print(f'吃了第{i}个苹果。')
    i += 1
