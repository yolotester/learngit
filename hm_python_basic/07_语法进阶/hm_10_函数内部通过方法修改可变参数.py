def test(num_list):

    print("函数内部执行代码开始。。。")

    # 使用方法修改列表的内容
    num_list.append(9)

    print(num_list)
    print("函数内部执行代码结束...")


# 同样会影响到外部的数据
gl_list = [1, 2, 3]
test(gl_list)
print(gl_list)