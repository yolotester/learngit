import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule

# 给导入的模块起别名后，可以直接使用： 模块别名.
DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)

print(CatModule.title)
print(DogModule.title)