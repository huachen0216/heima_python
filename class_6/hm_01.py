# -*- coding: utf-8 -*-

str1 = 'itheima'

for i in str1:
    if i == 'e':
        print('遇到e不打印 ')
        # break
        continue
    print(i)
else:
    print("for循环结束！")

