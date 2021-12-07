# 队列：完成进程间数据共享，队列只能存在于一个电脑中一个程序里多个进程间的数据共享
# redis：消息队列，能够存在于多个电脑中多个程序里，实现其他电脑发数据，我的电脑收数据
import multiprocessing
import time

def download_data_from_web(q):
    '''下载数据'''
    # 模拟从网上下载数据
    data = [11,22,33,44]

    # 向队列中写入数据

    for val in data:
        q.put(val)

        if q.full():
            break

    print('---下载器以及全部下载并写入到了队列中---')


def analysis_data(q):
    '''分析数据'''
    # 把取出来的数据放入列表中
    # 创建一个空列表
    analysis_data_append = list()

    # 从队列中获取数据
    # 不知道要取多少次数据，while true：一直循环取数据
    while True:
        data = q.get()
        analysis_data_append.append(data)

    # 判断什么时候为空，则结束将数据放入列表中
        if q.empty():
            break

    # 调试信息
    print(analysis_data_append)




def main():

    # 创建一个队列
    q = multiprocessing.Queue(3)  # 3，只允许往队列中存储3个数据，为空则根据硬件条件来决定存储多少数据

    # 创建多个进程，将队列的引用作为实参进行传递
    p1 = multiprocessing.Process(target=download_data_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()