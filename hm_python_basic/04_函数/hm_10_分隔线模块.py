def print_line(char, times):  # # 该模块中的 方法可以供外界使用
    '''
    打印 重复任意次数 任意符号的分隔线
    :param char: 分隔线的符号
    :param times: 分隔线的重复次数
    :return:
    '''
    print(char * times)


def print_lines(char, times):  # 该模块中的 方法可以供外界使用
    '''
    函数的嵌套调用，打印多条分隔线
    :param char: 分隔线的符号
    :param times: 分隔线的重复次数
    :return:
    '''
    row = 0
    while row < 5:
        print_line(char, times)  # 调用了print_line函数
        row += 1


name = "黑马程序员"  # 该模块中的 全局变量可以供外界使用