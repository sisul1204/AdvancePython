# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/7 22:40
# @file     : company.py
# @software : PyCharm

class Company:
    def __init__(self, employee_list):
        self.emplyee = employee_list

    def __getitem__(self, item):
        return self.emplyee[item]

    def __len__(self):
        return len(self.emplyee)

    def __str__(self):
        return ','.join(self.emplyee)

    def __repr__(self):
        return ','.join(self.emplyee)


# company = Company(['tom', 'jack', 'jane'])
# print(len(company))
# for em in company:
#     print(em)

company = Company(['tom', 'jack', 'jane'])
# print(company)
print(company)