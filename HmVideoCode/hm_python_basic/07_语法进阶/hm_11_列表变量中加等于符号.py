def test(num, num_list):

    print("函数内部执行代码开始。。。")

    # num = num + num
    num += num

    # 列表变量使用 += 本质上是num_list.extend(num_list)，调用了extend方法
    # 所以不会修改变量的引用，外部数据同样会发生变化
    num_list += num_list


    # 如果是下方这样，本质上是赋值语句，则不会影响到外部变量
    num_list = num_list + num_list

    print(num)
    print(num_list)

    print("函数内部执行代码结束...")


gl_num = 9
gl_list = [1, 2, 3]
test(gl_num, gl_list)
print(gl_num)
print(gl_list)