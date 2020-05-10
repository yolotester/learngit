# encoding=gbk
# else 与 while语句联合使用，素数只能被自身和1整除的数
# def ISodd(num):
#     count = num//2
#     while count >1:
#         if num % count == 0:
#             print('%d的第二个约数是%d：' % (num,count))
#             break
#         count -=1
#     else:
#         print('%d是素数' % num)
# num = int(input('请输入一个数字：'))
# ISodd(num)

# else 语句和try  except语句的联合使用
# try:
#     print(int('abd'))
# except ValueError as reason:
#     print('出错啦\n' + str(reason))
# else:
#     print('没有任何异常')
# 出错啦
# invalid literal for int() with base 10: 'abd'

# try:
#     print(int('123'))
# except ValueError as reason:
#     print('出错啦\n' + str(reason))
# else:
#     print('没有任何异常')
#
# 123
# 没有任何异常

# with语句用在文件中： 不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后,能够关闭打开了的文件句柄
try:
    with open('yolo.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦\n' + str(reason))