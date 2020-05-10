# 容器：数据的封装   函数：语句的封装   类：方法和属性的封装   模块：就是程序，一个.py结尾的文件
# import hello as he
# from helhewaytolearnmodulelo import hi
# import hello
# he.hi()   # 在python安装目录下新建了hello.py文件就是模块，在模块里定义了hi方法，可以导入该模块调用该方法
# hi()
# hello.hi()
# 导入模块三种方式：1、import 模块名  2 、from 模块名 import 函数名  3 import 模块名 as 别名
# !/usr/bin/env python3   注释可以让module.py文件直接在unix/linux/mac上运行
# -*- coding:utf-8 -*-     注释表示.py文件本身使用utf-8标准
'a test module'   # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释 可以用__doc__方法访问
__author__ = 'yolo'   # 显示作者名

'''
import sys   # 导入模块sys.py,就有了sys变量，使用这个变量就可以访问sys模块的所有功能
def test():
    args = sys.argv
   
# sys中有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，第一个元素是该.py文件的名称
    
    if len(args)==1:
        print('hello world!')
    elif len(args) ==2:
        print('hello,%s!' % args[1])
    else:
        print('too many arguments!')
if __name__ == '__main__':   # 在命令行运行module模块文件时，python解释器吧一个特殊变量\
    # __name__置为__main__,如果在其他地方导入该模块时，if判断将失败
    # if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()
'''
import sys
print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\nPython路径为：',sys.path,'\n')    # sys.path 包含了一个python解释器查找所需模块的路径的列表

# 搜索路径 1、当前目录  2、PYTHONPPATH下的每个目录 3、默认路径
# windows下典型的PYTHONPATH如下：
# set PYTHONPATH  = c:\python37\lib;
print(sys.path)      # 模块搜索路径存储在sys.path变量中，包含搜索路径

# 命名空间与作用域 :1.局部变量与全局变量重名,则会覆盖全局变量  2.python假设任何在函数内赋值的变量都是局部的
# 3,要给全局变量赋值,用global语句
# 变量是拥有匹配对象的名字(标识符),命名空间是个包含了变量名称们(键)和他们各自相应的对象们(值)的字典
# 举例说明
money = 2000
def borrow():
    global money   # 声明money为全局变量,解决问题
    money = money - 1    #  UnboundLocalError: local variable 'money' referenced before assignment
    name = 'yolo'
    locals()
    globals()
print(money)
borrow()
print(money)
print(globals())
print(locals()['__name__'])

# dir()方法返回一个列表,列表里包含模块里所有的类,方法,变量
content = dir(sys)
print(content)

# globals()和locals()方法
# 如果在函数内部调用locals(),返回的是所有能在该函数里访问的命名
# 如果在函数内部调用globals(),返回的是所有在该函数里能访问的全局名字
# 两个方法返回的类型都是字典,可以用keys()方法获得

# reload()方法，当一个模块被导入到一个脚本，模块顶层部分的代码只会执行一次
# 重新执行模块里顶层部分的代码，用reload（）方法


# 包（package）的概念  条件：1、一个文件夹，可以包含多个模块  2 、有一个__init__.py模块
# 包是一个分层次的文件目录结构，它定义了一个由模块，子包和子包下的子包等组成的python应用环境

# 例子文件结构
'''
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
'''
# import sound.effects.echo ,这会导入sound包中effects子包中echo模块，这样必须用全名去访问
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# from sound.effects import echo,直接导入echo模块，可以这样使用echo.echofilter(input, output, delay=0.7, atten=4)

# 直接导入一个函数或者变量：from sound.effects.echo import echofilter
# 可以这样使用，echofilter(input, output, delay=0.7, atten=4)

# 总结：
# from package import item,这种形式的时候，item即可以是子包，或者是包里面定义的类，方法，变量
# import item ，先去按照包导入，若没找到，按照模块导入，若还没找到，抛出ImportError的异常
# import item.subitem.subsubitem,除了最后一项，都必须是包，最后一项可以是包也可以是模块

# from sound.effects import *  ,是把__all__的列表变量作为包内容导入
# 作为包的作者，在更新了包之后，也要记得更新__all__中的内容

# 如果在结构中是一个子包，而你又想导入兄弟包，就得使用绝对的路径来导入
# from . import echo
# from .. import formats
# from ..filters import equalizer
# 无论是显示的还是隐士的相对导入，都是从当前模块开始。
# 主模块的名字永远是‘__main__’,一个python应用程序的主模块，应该总是使用绝对路径引用