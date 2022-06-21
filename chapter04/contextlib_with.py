# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/21 21:39
# @file     : contextlib_with.py
# @software : PyCharm

import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file close")


with file_open("test.txt") as f_open:
    print("file processing")
