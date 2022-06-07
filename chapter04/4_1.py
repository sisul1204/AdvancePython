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


animal = Cat
animal().say()
