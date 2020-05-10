# IDLE python自带集成开发环境，help-python doc  python官方文档，可去查询相关模块
# 善用IDLE
import timeit
import math
# from timeit import *   # 只会导入timeit.__all__中的类和方法

print(timeit.__doc__)   # 查看模块的文档注释

print(dir(timeit))      # 查看模块中各种类，方法，变量

print(timeit.__all__)   # 返回这个模块希望被外界调用的类和方法

print(timeit.__file__)  # 查看模块源代码的位置

print(help(timeit))   # 对模块快速上手的文档

print(math.__name__)  # 特殊变量返回模块的名字

if __name__ == '__main__':   # __name__属性来控制某程序块仅在自身模块运行时执行
    print('程序自己在执行')
else:
    print('我来自另一个模块')