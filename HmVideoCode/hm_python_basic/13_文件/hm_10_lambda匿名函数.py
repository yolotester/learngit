# 可写函数说明
# 作为表达式，lambda返回一个值（即一个新的函数）
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("想加后的值为：", sum(10, 20))
print("想加后的值为：", sum(20, 20))


L = [(lambda x: x ** 2),
     (lambda x: x ** 3),
     (lambda x: x ** 4)]
print (L[0](2), L[1](2), L[2](2))

D = {'f1': (lambda: 2 + 3),
     'f2': (lambda: 2 * 3),
     'f3': (lambda: 2 ** 3)}
print(D['f1'](), D['f2'](), D['f3']())