# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/7 23:32
# @file     : 4_1.py
# @software : PyCharm

class Cat:
    def say(self):
        print('i am a cat')


class Dog:
    def say(self):
        print('i am a dog')


class Duck:
    def say(self):
        print('i am a duck')


class Company:
    def __init__(self, employee_list):
        self.emplyee = employee_list

    def __getitem__(self, item):
        return self.emplyee[item]


company = Company(['green', 'blue'])

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

a = ['bobby1', 'bobby2']
b = ['bobby2', 'bobby']
name_tuple = ['bobby3', 'bobby4']
name_set = set()
name_set.add('bobby5')
name_set.add('bobby6')
a.extend(name_set)
a.extend(company)
print(a)
