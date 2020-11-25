print("hello world! ")

name_list = ['Tom', 'Lily', 'Rose']

name_list[0] = 'aaa'

print(name_list)

name_li2 = name_list.copy()

print(name_li2)

i = 0

while i < len(name_list):
    print(name_list[i])
    i += 1

for i in name_list:
    print(i)

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

print(dict1.items())
for key in dict1.keys():
    print(key)
    print(dict1.get(key))
    print("==============")

for key, value in dict1.items():
    print(f'{key} = {value}')


