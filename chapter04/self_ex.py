# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/20 21:56
# @file     : self_ex.py
# @software : PyCharm


from chapter04.class_method import Date


class Person:
    """
    人
    """
    name = 'user'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('慕课网')
    print(user.__dict__)
    user.__dict__['school_address'] = '杭州市'
    print(user.__dict__)
    print(Person.__dict__)
    print(user.name)
    print(dir(user))
