# 创建Thread类的对象两种方式：1、Thread（target=函数名）
# 2、继承于Thread类的自定义类的实例化对象t，当t调用start（）时，即自动先调用类中run（）
# 适合情况：一个线程里的内容比较复杂，而且分成多个函数来做，则封装成类，用类的实例化对象来调用方法


import threading
import time


class MyThread(threading.Thread):  # 继承Thread类
    def run(self):
        self.sing()  # 创建并执行sing（）的子线程
        for i in range(3):
            time.sleep(1)
            msg = "i'm " + self.name + '@ ' + str(i)  # name属性中保存的是线程的名字
            print(msg)

    def sing(self):
        for i in range(5):
            time.sleep(1)
            msg = "i'm  threading " +  '@ ' + str(i)  # name属性中保存的是线程的名字
            print(msg)


if __name__ == "__main__":
    t = MyThread()
    t.start()  # 创建并执行run（）的子线程，自动调用run（）方法


