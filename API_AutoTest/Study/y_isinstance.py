#! usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.runoob.com/python/python-func-isinstance.html
'''
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
'''
'''
语法：
isinstance(object, classinfo)
classinfo可以是 int，float，bool，complex，str(字符串)，list，dict(字典)，set，tuple
'''


class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A      # returns True
print(isinstance(B(), A))  # returns True
type(B()) == A      # returns False