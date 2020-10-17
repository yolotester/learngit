# import 导入模块，若模块中代码已经更改，想要导入已经更改后的模块，可以from imp import reload,然后reload（模块名）
# 多模块开发，main.py，全是调用其他模块的函数，common.py,各个模块中共有的属性，recv_data.py,完成某一功能的模块
# 多继承
# 方法名 就是 变量名，方法名相同的方法会被覆盖