# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/20 20:53
# @file     : class_method.py
# @software : PyCharm

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year}/{self.month}/{self.day}'

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2018, 10, 1)
    print(new_day)

    date_str = '2018-10-02'
    print((Date.parse_from_string(date_str)))

    date_str = '2018-10-03'
    print(Date.from_string(date_str))
