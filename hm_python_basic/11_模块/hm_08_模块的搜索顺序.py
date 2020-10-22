import random

# Python 中每一个模块都有一个内置属性 __file__ 可以 查看模块 的 完整路径
print(random.__file__)  # C:\Users\yolo\AppData\Local\Programs\Python\Python37\lib\random.py
rand = random.randint(0, 10)

print(rand)