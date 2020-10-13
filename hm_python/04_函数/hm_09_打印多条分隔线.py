def print_line(char, times):
    '''
    打印 重复任意次数 任意符号的分隔线
    :param char: 分隔线的符号
    :param times: 分隔线的重复次数
    :return:
    '''
    print(char * times)


def print_lines(char, times):
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


print_lines("-", 10)