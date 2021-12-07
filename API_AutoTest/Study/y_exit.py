#! usr/bin/env python
# -*- coding: utf-8 -*-


# https://blog.csdn.net/index20001/article/details/74294945
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
import sys
import jsonpatch


def age():
    age = 17

    if age < 18:

        # exits the program
        sys.exit("Age less than 18")
    else:
        print("Age is not less than 18")


def sys_exit():
    try:
        sys.exit(0)
    except:
        print('Program is dead.')
    finally:
        print('clean-up')

doc = {'foo': 'bar'}
patch = [{'op': 'add', 'path': '/baz', 'value': 'qux'}]
other = jsonpatch.apply_patch(doc, patch)
print(other)

sys_exit()