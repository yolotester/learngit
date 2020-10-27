class Dog(object):

    @staticmethod
    def run():

        # 不访问实例属性/类属性时，可以定义为静态方法
        print("小狗跑啊跑...")


# 调用静态方法  --  类名.静态方法名
Dog.run()