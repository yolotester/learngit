import hm_01_测试模块1
import hm_02_测试模块2

# 使用的是： 模块名.
# 调用其他模块的方法
hm_01_测试模块1.say_hello()
hm_02_测试模块2.say_hello()

# 使用其他模块创建对象
dog = hm_01_测试模块1.Dog()
cat = hm_02_测试模块2.Cat()
print(dog)
print(cat)

# 访问其他模块的全局变量
print(hm_01_测试模块1.title)
print(hm_02_测试模块2.title)