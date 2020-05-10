# 函数就是完成某一功能的代码块     调用函数就是对代码块的多次复制   参数可以使得函数个性化
# 函数的定义   无参
def myFirstFunc():
    print('我创建的第一个函数')
    print('哈哈哈哈哈哈哈')

# 函数的调用
myFirstFunc()
myFirstFunc()

# 有一个参数      name：形参，只是一个形式，表示占据一个参数位置    ‘doudou’：实参
def mySecondFunc(name):
    print(name + '我很好')

mySecondFunc('doudou')

# 函数的返回值  return,返回值需要一个变量接收
def add(num1,num2):
    return num1 + num2
sum = add(5,6)
print(sum)


# 形参：函数定义过程中出现的参数
# 实参：函数在调用过程中传入的具体值

# 关键字参数,指定形参传入实参
def SaySome (name , words):
    print(name + '>' +words)

SaySome(words='yolo',name='改变豆豆的心意')

# 默认参数放在形参最后面，定义了默认值的参数,没有传入实参,则会使用默认值.若传入实参,则使用传入的值
# 有预设值的参数不能先于无预设值的参数赋值,会报错
def SayAny(name = 'yolo',words = '改变豆豆的心意') :
    print(name + '>' +words)

SayAny()
SayAny('张小白','改变小豆豆')
SayAny(words='改变豆豆的心意',name='yolo1')

# 收集参数   可传多个参数
def test(*params):
    print('参数的长度：', len(params))
    print('第二个参数：',params[1]) # 通过索引访问

# TypeError: can only concatenate str (not "int") to str
test(1,5,'ad',3.21)

# 有除了收集参数外的参数，需要用关键字参数
def test(*params,exp):
    print('参数的长度：', len(params))
    print('第二个参数：', params[1],exp)

# TypeError: test() missing 1 required keyword-only argument: 'exp'
test(1, 5, 'ad', 3.21,exp='yolo')


# python中只有函数（有返回值,或者返回None），无过程（无返回值）
# 无返回值的例子
def hello():
    print('hello word')
temp = hello()
print(hello())
print(temp)

# python可返回多个值,有返回值就需要变量来接收
def word():
    return [1,'wo',3.14],52
lt , sum = word()
print(lt,sum)   # 函数的返回值是个列表

def num(x,y):
    n = x + y
    z = x - y
    u = x * y
    return n,z,u
sum , mul ,che = num(8,5)  # 有几个返回值用几个变量接收
print(sum,mul,che)

re = num(8,5)  # 一个变量接收多个返回值,返回的是元组,可用索引访问
print(re)
print(re[0])





# 内嵌函数     fun2（）定义和调用都在fun1（）里，且不能跨过fun1（）来调用fun2（）
def fun1():
    print('fun1()正在被调用')
    def fun2():
        print('fun2()正在被调用///')
    fun2()

fun1()
'''
# 闭包   funy为内部函数，且funy的外部空间为funx的整个空间，称funy为闭包
def funx (x):
    def funy (y):
        return x * y
    return funy
i= funx(8)
print(type(i))
print(i(5))
# funx(8)(5)

# 举例二
def fun1():
    x =5
    def fun2():
        x *= x
        return  x
    return fun2()
# 调用fun1（）会出错，因为在内部函数修改了外部函数得变量
# fun1（）
# 解决办法一，用容器接收，容器（元组字符串列表）不存放在栈空间，python回收机制不会回收
def fun3():
    x[0] =5
    def fun4():
        x[0] *= x[0]
        return  x
    return fun4()
fun3()

# 解决方法二    使用关键字nonlocal
def fun5():
    x =5
    def fun6():
        nonlocal x
        x *= x
        return  x
    return fun6()
fun5()

'''







# lambda表达式，匿名函数
# 一个参数
g = lambda x : 2*x + 1
print(g(5))

# 两个参数
g = lambda x ,y: x + y
print(g(5,6))

# 作用：1、写一些执行脚本，可以省下定义和调用函数的过程，使得代码更精简
# 2、不需要考虑函数命名
# 3、简化代码的可读性


# 两个重要的BIF   filter(function and None,literable)过滤器：过滤功能,返回的是1和真值
# 举例None
print(filter(None,[1,0,False,True]))
print(list(filter(None,[1,0,False,True])))

# 举例function
def odd(x):
    return x % 2
temp = range(10)
show = filter(odd,temp)
print(list(show))

print(list(filter(lambda x : x % 2 ,range(10))))


# 映射 map（function ,literable） 把可迭代序列中每个元素作为实参传入function中
print(list(map(lambda x : x *2,range(10))))
















