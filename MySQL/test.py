#!/usr/bin/env python
# encoding : UTF-8
"""
@author : Xil-max
@file   : test.py
@time   : 2021/12/31 10:50
@Description : TODO
"""


def f(iterator):
    tup = []
    for x in iterator:
        temp = (x, len(x))
        print("temp=", temp)
        tup.append(temp)
    return tup


def new_data(d):
    b = []
    for i in d:
        a = i.split(" ")
        b.append(a)
    print(b)


data = ["hello scala", "salmon hello", "salmon hello", "rat hello", "elephant hello"]
new_data(data)
print(new_data(data))
