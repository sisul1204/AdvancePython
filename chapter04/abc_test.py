# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/8 21:10
# @file     : abc_test.py
# @software : PyCharm
from collections.abc import Sized


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['bbb1', 'bbb2'])
print(hasattr(com, '__len__'))
print(isinstance(com, Sized))