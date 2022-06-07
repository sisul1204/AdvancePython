# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/7 23:16
# @file     : vector.py
# @software : PyCharm

class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'


first_vector = MyVector(1, 2)
second_vector = MyVector(2, 3)
print(first_vector+second_vector)
