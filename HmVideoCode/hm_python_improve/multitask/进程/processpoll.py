# 进程池：可以指定一个最大进程数，然后执行任务，达到循环利用进程的作用
# 什么时候用进程池:任务数不确定的时候,用进程池
from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print('%s 开始执行,进程号为% ' % (msg, os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, '执行完毕,耗时%0.2f ' % (t_stop - t_start))


if __name__ == '__main__':

    po = Pool(3)  # 创建进程池,指定最大进程数为3
    for i in range(0,10):
        # Pool().apply_async(要调用的目标,(传递给目标的函数元组,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))


    print('======start =======')
    po.close()  # 关闭进程池,关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成,必须放在close语句之后
    print('======stop=======')