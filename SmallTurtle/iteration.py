from collections.abc import Iterable,Iterator
# 迭代类似于循环，每一次重复的过程就叫迭代。上一次迭代的结果，将用作下一次迭代的初始值
# 提供迭代方法的容器，称为迭代器。通常接触迭代器的是序列包含（列表，元组，字符串，字典，集合）和生成器和带yield的generator function
# 字符串即是容器又是迭代器，通过for语句从迭代器中一个一个取出元素
# 使用for语句进行迭代
for i in "yolo":
    print(i)

# 字典和文件也支持迭代
dict = {'yolo':'doudou','happy':'day'}
for each in dict:
    print('%s -> %s' % (each,dict[each]))

# 两个BIF，调用iter（），则会返回一个迭代器，调用next（）依次返回迭代器中的值如果迭代器没有值可以返回，则抛出一个StopIteration的异常
# 举例说明
str  = 'yolo'
it = iter(str)   # <class 'str_iterator'>,将字符串str，变为迭代器
print(type(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))     # StopIteration 迭代器中没有元素可以返回，抛出此异常

# for语句工作原理
str = 'yolo'
it = iter(str)
while True:
    try:
        each = next(it)
    except StopIteration as e:
        break
    print(each)

# 两个魔法方法  __iter__()返回迭代器本身,__next__()设置迭代规则，迭代器不跳出，会一直迭代下去
# 迭代斐波那契数列
class Fib:
    def __init__(self,n=10):  # n控制迭代的最大值

        self.a = 0
        self.b = 1
        self.n = n
    # 调用__iter_方法

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b= self.b,self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

def main():
    fib = Fib()
    for each in fib:
        print(each)

if __name__ == '__main__':
    main()

# isinstance（）判断一个对象是否是Iterable（可迭代的）对象
print(isinstance([],Iterable))
print(isinstance('abx',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

# isinstance()判断一个对象是否是Iterator（迭代器）对象
# 迭代器是Iterator对象，list，str，dict是Iterable对象不是Iterator对象，可使用iter方法变成Iterator对象
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abx'),Iterator))



