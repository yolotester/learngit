# encoding=gbk
# else �� while�������ʹ�ã�����ֻ�ܱ������1��������
# def ISodd(num):
#     count = num//2
#     while count >1:
#         if num % count == 0:
#             print('%d�ĵڶ���Լ����%d��' % (num,count))
#             break
#         count -=1
#     else:
#         print('%d������' % num)
# num = int(input('������һ�����֣�'))
# ISodd(num)

# else ����try  except��������ʹ��
# try:
#     print(int('abd'))
# except ValueError as reason:
#     print('������\n' + str(reason))
# else:
#     print('û���κ��쳣')
# ������
# invalid literal for int() with base 10: 'abd'

# try:
#     print(int('123'))
# except ValueError as reason:
#     print('������\n' + str(reason))
# else:
#     print('û���κ��쳣')
#
# 123
# û���κ��쳣

# with��������ļ��У� �����ڴ����ļ��������Ƿ����쳣�����ܱ�֤ with ���ִ����Ϻ�,�ܹ��رմ��˵��ļ����
try:
    with open('yolo.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('������\n' + str(reason))