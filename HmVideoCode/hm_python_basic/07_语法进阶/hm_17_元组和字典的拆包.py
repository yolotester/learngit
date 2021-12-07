def test(*args, **kwargs):

    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name":"小明", "age":18}
# test(gl_nums, gl_dict)  这种方式，都会传递给args参数

# 如果希望
# 将一个元组变量， 直接传递给args
# 将一个字典变量， 直接传递给kwargs
# 拆包语法
test(*gl_nums, **gl_dict)