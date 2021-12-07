# tcp：面向连接的、可靠的、基于字节流的协议，tcp通信三个步骤:创建连接，数据传送，终止连接
# 创建连接：三次握手，以保证数据可靠传输，四个原因：tcp采用发送应答机制，超时重传，错误校验，流量控制和阻塞管理
# tcp客户端

import socket


def main():

    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 链接服务器
    # tcp_socket.connect('192.168.2.1',5555)  作用同下面四行
    server_ip = input('请输入要链接的服务器的IP：')
    server_port = int(input('请输入要链接的服务器的port：'))
    server_addr  = (server_ip,server_port)  # 元组存储数据
    tcp_socket.connect(server_addr)  # 默认是阻塞的，直到tcp三次握手结束才解阻塞，才能发数据

    # 发送数据
    send_data = input('请输入你要发送的数据：')
    tcp_socket.send(send_data.encode('utf-8'))  # send()方法数据格式为字节型数据，需要编码

    # 接收数据
    tcp_socket.recv(1024)  # 收到的数据为普通数据

    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
