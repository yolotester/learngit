# 协同程序：就是可以运行的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继续或者重新开始
# 生成器：能够一边循环一边计算的机制
# 带yield的生成器是特殊的迭代器
# 把列表推导式中的[],改成（），就创建了一个generator生成器
# 举例说明
def myGen():
    print('生成器被执行////')
    yield 1
    yield 2
mg = myGen()
print(next(mg))
print(next(mg))
# print(next(mg))   抛出异常StopIteration

# 用生成器写斐波那契数列
def fib():
    a = 0
    b = 1
    while True:
        a,b = b ,a +b
        yield a     # 函数可以暂停

def main():
    for each in fib():
        if each > 100:
            break
        print(each,end = '\n ')   # end 语句，使得打印不会换行
if __name__ == '__main__':
    main()