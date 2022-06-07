# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/7 21:30
# @file     : all_is_object.py
# @software : PyCharm

def ask(name='tom'):
    print(name)


class Person:
    def __init__(self):
        print('jack')


def print_type(item):
    print(type(item))


def decorator_func():
    print("desc start")
    return ask


my_ask = decorator_func()
my_ask('jack')

# obj_list = [ask, Person]
# for item in obj_list:
#     print_type(item)
