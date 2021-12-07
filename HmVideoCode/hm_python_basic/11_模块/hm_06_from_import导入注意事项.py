from hm_01_测试模块1 import say_hello as module1_say_hello
from hm_02_测试模块2 import say_hello

# 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
# 调用的是 hm_02_测试模块2 中say_hello()方法
say_hello()

# 发现冲突后，可以使用 as 关键字 给其中一个工具起一个别名
module1_say_hello()