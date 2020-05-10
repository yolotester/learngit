# 容器类型的协议
# 如果你定制的容器是不可变的(例如:字符串\元组),只需要定义__len__(),和__getitem__()方法
# 如果你希望定制的容器是可变的,除了定义__len__(),__getitem__()方法,还需要定义__setitem__().__delitem__()方法
# __len__(self),定用义当被len()调时,返回容器中元素的个数
# __getitem__(self,key),获取容器中指定元素的行为,相当于self[key]
# __setitem__(self,key,value),设置容器中指定元素的行为,相当于self[key]=value
# __delitem__(self,key),删除容器中指定元素的行为,相当于del self[key]
# __iter__(self),定义当迭代容器中的元素的行为
# __reversed__(self),定义当被reversed()调用时的行为
# __contains__(self,item),定义当使用成员测试运算符(in或者not in)时的行为

# 练习.编写一个不可改变的自定义列表,要求记录列表中每个元素被访问的次数
class Countlist:
    def __init__(self,*args): # *args  表示传入的是可变数量的参数
        # 列表推导式,记录列表中元素的值
        self.values = [x for x in args]
        # 把每个元素的下标,作为字典的键.字典的值,就是访问次数.想要知道下标所对应的元素被访问多少次,直接访问字典就行
        # 初始化字典 fromkeys
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] +=1
        return self.values[key]

count = Countlist(1,2,3,5,6)
print(count[1])
print(count.count)

# variable = [out_exp_res for out_exp in input_list if out_exp == 2]
# 列表推导式完整版
# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代input_list将out_exp传入out_exp_res表达式中。
# if out_exp == 2：根据条件过滤哪些值可以。