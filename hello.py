import json
import math
from enum import Enum
from functools import reduce

import os

import pickle

from liufeng import index
from liufeng.Student import Student
from liufeng.Weekday import Weekday

__author__ = "liu-feng"

if __name__ == '__main__':
    print("Hello world.")

'''
 Hello Python 
'''

"""
 Hello World
"""

print("上面是一条注释")

# Hello Python 3.6.4

print('I\'m OK.')
print(r'T "IM OK " r\n\r ')
print('''
    hello world
    hello python3.6
''')

a = 10

PI = 3.14

print(PI)

PI = a

print(PI)

print(10 / 3)

print(chr(86))

print(ord('中'))

print('\u4e2d\u6587')

print('%.2f %s' % (3.141592653, 'liufeng'))
print('hello {0} {1:.3f}'.format('liu-fneg', 3.141592653))

s1 = 72
s2 = 85

r = (s2 - s1) / s1
print('小明的成绩提升了%.1f' % r)

arr = [1, 'liufeng', 0.5]
print(len(arr))

count = 0
for i in range(1, 101):
    count += i

print(count)
count = 0
i = 0
while i < 101:
    count += i
    i += 1

print(count)

# while True:
#     print('hello')


a = abs
print(a(-1))

a = 100
print(type(hex(a)))


def quadratic(a, b, c):
    if a == 0:
        return
    x = b * b - 4 * a * c
    if x < 0:
        return
    elif x == 0:
        return -b / 2 * a
    else:
        return (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a), (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    pass


print(quadratic(1, 2, 1))


def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s
    pass


print('    hello world   d      ')
print(trim('    hello world   d      '))

L = ['Hello', 'World', 18, 'Apple', None]

L2 = (s.lower() for s in L if isinstance(s, str))

for x in L2.__iter__():
    print(x)


def add(x, y, f):
    return f(x) + f(y)
    pass


print(add(3, 5, abs))


def fx(x):
    return x * x


print(list(map(fx, (x for x in range(10)))))

arr = ['adam', 'LISA', 'barT']
print(list((s.capitalize() for s in arr if isinstance(s, str))))


def prod(L=[]):
    def qiuhe(x, y):
        return x + y

    def qiuji(x, y):
        return x * y

    return reduce(qiuhe, L), reduce(qiuji, L)
    pass


print(prod([1, 2, 3, 4, 5]))


# 利用filter去除序列中的空格
def qukongge(L):
    def kongge(s):
        return s and s.strip()

    return reduce(lambda x, y: x + y, filter(kongge, L))
    pass


print(qukongge('        hell o world . '))


# 利用filter求素数
def _old_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _old_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


#   利用filter求回数
def is_palindrome(n):
    a = list(str(n))
    b = tuple(a)
    a.reverse()
    b = list(b)
    return a == b


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

# 使用sorted进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda t: t[0]))
print(sorted(L, key=lambda t: t[1], reverse=True))

# 利用闭包返回一个计数器函数


# 匿名函数
print(list(filter(lambda x: x % 2 == 1, range(20))))

print(index.index())

student1 = Student('liufenng', 25)
student1.set_age(101)
print(type(student1).__name__)

print(dir(student1))

# student2 = Student('zhangsan', 21)

print(Student.cns)

print(student1.__str__())

JAN = 1
FEB = 2

for name, member in Weekday.__members__.items():
    print('%s=>%s' % (name, member.value))

try:
    10 / 0
    pass
except ZeroDivisionError as e:
    print(e)
    pass
finally:
    print('继续...')
    pass
d = dict(name='liu-feng', age=20, score=88)
# f = open("./liufeng/dump.txt", 'wb')
# pickle.dump(d, f)
# f.close()

print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(dict(json.loads(json_str)))
