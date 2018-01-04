#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/4 13:36

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


class Student:
    cns = 0

    __slots__ = ('__name', '__age')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.cns += 1
        pass

    def __str__(self):
        return 'Student object (name=%s)' % Student.__name__

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            return
