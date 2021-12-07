# 文件夹的拷贝
import os
import multiprocessing


def copy_file(q,file_name,old_files_name,new_files_name):
    '''复制文件'''
    # print('-------->模拟拷贝文件: 从%s----%s 文件名是:%s ' % (old_files_name,new_files_name,file_name))
    # 打开原文件夹,读取原文件夹内容
    f_old = open(old_files_name + '/' + file_name, "rb")
    content = f_old.read()
    f_old.close()

    # 写入新文件中
    f_new = open(new_files_name + '/' + file_name, 'wb')
    f_new.write(content)
    f_new.close()

    # 如果拷贝完成文件,则向队列中写入一个消息
    q.put(file_name)


def main():
    # 获取要拷贝的文件夹名字
    old_files_name = input('请输入要拷贝的文件夹名字:')

    # 创建一个新文件夹,try语句,判断新文件夹若存在,则pass.不抛出异常
    try:
        new_files_name = old_files_name + '附件'
        os.mkdir(new_files_name)
    except:
        pass

    # 获取要拷贝的文件夹中所有文件的名字
    all_file_name = os.listdir(old_files_name)
    print(all_file_name)

    # 复制文件
    # 创建进程池
    po = multiprocessing.Pool(5)

    # 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 向进程池添加  copy文件的任务
    for file_name in all_file_name:
        po.apply_async(copy_file, args=(q,file_name,old_files_name,new_files_name))

    po.close()
    # po.join()  # 主进程结束,则代码结束
    file_num = len(old_files_name)  # 测试所有的文件个数
    copy_ok_num = 0  # 变量作为copy好的文件数,初始化为0
    while True:  # 让主进程一直执行
        file_name = q.get()
        # print('已经完成拷贝 : %s ' % file_name)
        copy_ok_num += 1
        print('\rcopy 的进度为: %.2f %%' % (copy_ok_num * 100/(file_num-1)), end='')


        if copy_ok_num >= file_num:
            break


if __name__ == '__main__':
    main()