# 互斥锁可能会产生死锁
# 避免死锁的方法：1、添加超时时间   2、程序设计时要尽量避免（银行家算法）

# 多任务版udp聊天器

import socket
import threading


def send_msg(udp_socket,dest_ip,dest_port):
    '''发送消息'''
    while True:

        send_data = input('请输入要发送的数据：')
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))


def recv_msg(udp_socket):
    '''接收数据'''
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('%s : %s' % (str(recv_data[1])),recv_data[0].decode('utf-8'))


def main():
    '''udp聊天器总体步骤
    '''
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定本地信息（ip，端口）
    udp_socket.bind(('',7788))

    # 绑定目标信息（ip，端口）
    dest_ip = input('请输入目标IP：')
    dest_port = int(input('请输入目标port：'))

    t_send = threading.Thread(target=send_msg, args=(udp_socket,  dest_ip,dest_port))
    t_recv = threading.Thread(target=recv_msg,args=(udp_socket))
    t_send.start()
    t_recv.start()


    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()