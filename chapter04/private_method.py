# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/20 21:43
# @file     : private_method.py
# @software : PyCharm

from chapter04.class_method import Date

class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2022 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990, 10, 21))
    print(user._User__birthday)
    print(user.get_age())
