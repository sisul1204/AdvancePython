# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/8 21:37
# @file     : instance_type.py
# @software : PyCharm

class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(type(b))
print(id(type(b)))
print(id(B))