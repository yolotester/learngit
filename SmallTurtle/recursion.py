# 递归   函数调用函数的过程 recursion
# 函数的方式求阶乘
'''
def func(n):
    result = n
    for i in range(1,n):
        result *= i
    return  result
number = int(input('请输入一个整数：'))
nu2 = func(number)
print('%d 的阶乘为%d;'% (number,nu2))

# 递归方式   递归条件：1、调用函数自身  2、设置了自身正确的返回值，有停止的条件
def func1(n):
    if n == 1:
        return  1
    else:
        return n * func1(n - 1)
number = int(input('请输入一个正整数：'))
nu2 = func1(number)
print('%d 的阶乘为%d' % (number,nu2))
'''
'''
# 斐波那契数列 递归方式(分治思想)  效率会变低
def fibna(n):
    if n < 1:
        print('输入有误哦')
        return  -1
    if n == 1 or n == 2:
        return  1
    else:
        return fibna(n-1) + fibna(n - 2)
result = fibna(20)
if result != -1:
    print('总共有%d只小兔子' % result)

# 迭代方式
def fib(n):
    n1=1
    n2=1
    n3=1
    if n <1:
        print('输入有误哦')
        return  -1
    if (n - 2) >0:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        n -=1

    return n3
result = fibna(20)
if result != -1:
    print('总共有%d只小兔子' % result)
'''
# 汗诺塔游戏
def hanot(n,x,y,z):
    if n == 1:
        print(x , '-> ',z)

    else:
#         将前n-1个盘子从x移动到y上
        hanot(n-1,x,z,y)
 #        将最底下的那个盘子从x移动到z上
        print(x,'->',z)
#          将y上n-1个盘子从y移动到z上
        hanot(n-1,y,x,z)
n = int(input('请输入汗诺塔层数;'))
hanot(n,'X','Y','Z')