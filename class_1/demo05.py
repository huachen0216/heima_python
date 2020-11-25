s1 = {10, 20}
print(s1)

s1.update([100, 200])
s1.update('abc')
print(s1)

s2 = {10, 30, 20, 10, 30, 40, 30, 50}
print(s2)
print(type(s2))

list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}

print(type(tuple(list1)))
print(type(tuple(s1)))

t1 = ('a', 'b', 'c', 'd', 'e')
s1 = {100, 200, 300, 400, 500}
t2 = ('a', 'b', 'c', 'd', 'e')

print(list(t1))
print(list(s1))

print(type(list(t1)))
print(type(list(s1)))

# print(t1.__add__(t2))

list2 = [i for i in range(1, 11, 1)]
print(list2)

num = 5


def testA():
    global a
    a = 200
    print(a)


testA()


def return_num():
    return 1, 2

print(return_num)