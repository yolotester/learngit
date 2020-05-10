# encoding=gbk
# �����йص����ú���
# issubclass(class,classinfo)    �ж�һ�����Ƿ�����һ���������
# 1.һ����Ĭ��Ϊ�����һ������
# 2.classinfo�������������ɵ�Ԫ��,ֻҪclass�������κ�һ����ѡ�������,�򷵻�True
class A:
    pass
class D:
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,D))

# isinstance(object,classinfo)  ���һ��ʵ�������Ƿ�����һ����
# 1.�����һ���������Ƕ���,����Զ����false
# 2.����ڶ�������������������������ɵ�Ԫ��,���׳�һ��TypeError���쳣
b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(isinstance(b,D))
print(isinstance(b,(A,B)))

# hasattr(object,name)   ���name�Ƿ��Ƕ����������
class C:
    def __init__(self,x=0):
        self.x = x
c = C()
print(hasattr(c,'x'))
# print(hasattr(c,x))     NameError: name 'x' is not defined

# getattr(o,name,[default])   ���name�Ƿ��Ƕ����������,��û�и�������������Ĭ��ֵ,����ʾĬ��ֵ
print(getattr(c,'x'))
# print(getattr(c,'y'))        AttributeError: 'C' object has no attribute 'y'
print(getattr(c,'y','�������ʵ����Բ�����...'))

# setattr(o,name,value)       ���name�Ƿ��Ƕ����������,��û�и�������������valueֵ,��Ϊ�ö��󴴽��������Ҹ�valueֵ
setattr(c,'z','yolo')
print(getattr(c,'z'))

# delattr(o,name)             ɾ������ָ��������,��������û�и�����.�ᱨ��AttributeError���쳣
# print(delattr(c,'l'))         AttributeError: l
print(delattr(c,'x'))
print(hasattr(c,'x'))

# property(fget=None,fset=None,fdel=None)  #
class C:
    def __init__(self,size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size =value
    def delSize(self):
        del self.size
    x= property(getSize,setSize,delSize)

c = C()
print(c.getSize())
print(c.x)   #fget
c.x = 18    #fset
print(c.getSize())
del c.x    #fdel
print()


