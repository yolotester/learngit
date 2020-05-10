# -*- coding: gbk -*-

# AssertionError  ����ʧ��
passion = ['yolo']
assert len(passion) >0
# assert len(passion)>2

# AttributeError  ���Է���δ֪�Ķ�������
# passion.fishc()   AttributeError: 'list' object has no attribute 'fishc'

# Index Error  ����������Χ
# passion[3] = 1        IndexError: list assignment index out of range

# KeyError   �����ֵ��в����ڵļ�
impotence ={'yolo':'doudou','doudou':'yolo'}
# print(impotence['yolO'])     KeyError: 'yolO'
# �������������Ҳ��������쳣
print(impotence.get('Yolo'))   # ����None�������ᱨ��

# NameError   ���Է��ʲ����ڵı���
#print(a)             NameError: name 'a' is not defined

# OSError  ����ϵͳ�������쳣(����һ���ܳ�)
# creativity = input('������һ���ļ�����')
# f = open(creativity)
# for each_line in f:
#     print(each_line)
#  FileNotFoundError: [Errno 2] No such file or directory: 'readme'

# SyntaxError   python�﷨����
# print 'yolo'    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('yolo')?

# TypeError  ��ͬ���ͼ����Ч����
# print(1 + '1')     TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ZeroDivisionError   ����Ϊ��
# print(5/0)    ZeroDivisionError: division by zero


# �쳣���  try-except����try...finally���,���ԽӶ��except���/�����쳣�����䲻�ᱻִ��
# try:
#     ��ⷶΧ
# except Exception[as reason]:
#     �����쳣��exception����Ĵ������
# finally:
#     ������ζ��ᱻִ�еĴ���

# ����
# try:
#      investment= open('yolo.txt')
#     print(investment.read())
#     investment.close()
# except OSError:
#     print('�ļ�������......')

# try:
#
#     # int('adc')   ValueError: invalid literal for int() with base 10: 'adc'
#     sum = 1 + '1'
#     investment = open('yolo.txt')
#     print(investment.read())
#     investment.close()
# # except OSError as reason:
# #     print('�ļ�������......\n�����ԭ���ǣ�' + str(reason))
# # except TypeError as cause:
# #     print('���ͳ�����......\n�����ԭ���ǣ�' + str(cause))
# except (OSError,TypeError):
#     print('������////')

try:
    bartender = open('yolo.txt','w')
    print(bartender.write('YYYYYOOOOOLLLLLOOOOO'))
    sum = 1 + '1'
    bartender.close()
except (OSError,TypeError):
    print('������////')
finally:
    bartender.close()

# raise��䣬�����쳣
raise ZeroDivisionError