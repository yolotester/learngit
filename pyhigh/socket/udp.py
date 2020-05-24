# 网络的目的：即进程之间的通信，传输数据
# IP地址：用于标记网络上的唯一一台电脑
# 本地连接，wifi都属于网卡，我可以选择用哪个网卡进行通信  sudo ifconfig 网卡名 down/up
# IP V4的地址：共有256*256*256*256个ip地址，IP地址：网络号+主机号（0，255不能用）
# 端口：确定数据传输给电脑的哪个程序（进程：运行起来的程序）1、知名端口0-1023不随便用。80：http服务，21：ftp服务  2、动态端口范围：1024-65535，Linux：netstat -an 查看端口状态
# 通信基本过程中必须数据字段：content，dest_ip ,src_ip ,dest_port,src_port
# 单工：收音机   半双工：对讲机   全双工：电话
# socket：套接字，有tcp socket ，udp socket，属于全双工
import socket

def main():

    # 创建udp套接字
    # AF_INET,用于internet进程间通信     SOCK_DGRAM：数据报套接字，用于udp协议   SOCK_STREAM:流式套接字，用于tcp协议
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_dgram)

    # 元组local_ipport绑定自己本地的IP和端口号
    local_ipport = ('',7788)
    udp_socket.bind(local_ipport)

    # 循环接收数据
    # while True:
    #     # 接收数据
    #     # 1024表示能收到的最大1024字节数据，用变量recv_data存储的是一个元组（发送方数据，（发送方IP，发送发port））
    #     recv_data = udp_socket.recvfrom(1024)
    #     recv_msg = recv_data[0]  # 存储接收的数据
    #     send_addr = recv_data[1]  # 存储发送方的地址信息，是一个元组.%s 格式化输出，需要用str（）转换为字符串
    #
    #
    #     # 打印接收到的数据和用于调试的输出
    #     print('%s : %s' % (str(send_addr),recv_msg.decode('utf-8')))  # 格式化输出数据
    #     print('--------1111-------')




    # 循环发送数据
    while True:

        # 从键盘获取数据
        send_data = input('请输入要发送的数据：')

        # 如果输入exit，则退出程序,break 跳出循环
        if send_data == 'exit':
            break

        #  使用套接字发送数据
        # 元组dest_ipport:存储的是目标ip和port
        dest_ipport = ('192.168.1.1',8080)
        # udp_socket.sendto(b'hello,i am yolo',dest_ipport)   不够通用
        udp_socket.sendto(send_data.encode('utf-8'), dest_ipport)




    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()


