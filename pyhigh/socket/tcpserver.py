# tcp服务器
import socket


def main():

    # 创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建tcp套接字

    # 绑定本地信息（ip/port）
    local_ip = input('请输入服务器的ip：')
    local_port = int(input('请输入服务器的port：'))
    local_addr = (local_ip,local_port)
    tcp_server_socket.bind(local_addr)

    # 让默认的套接字由主动变为被动 listen,监听套接字，只负责等待有新的客户端进行连接
    tcp_server_socket.listen(128)

    # 循环为客户端连接
    while True:

        # 等待客户端的连接   accept产生的新的套接字用来为客户端服务
        # accept 默认阻塞，直到有客户端连接
        print('等待一个新的客户端的到来:' )
        new_client_socket, client_addr = tcp_server_socket.accept()  # 返回值是个元组，参数个数固定，适合拆包

        print('一个新的客户端已经到来%s ' % str(client_addr))

        # 循环为该客户端服务
        while True:

            # 接收客户端发送的数据
            recv_data = new_client_socket.recv(1024)  # 默认阻塞，等待客户端发送数据
            print('客户端发送过来的数据是%s' % recv_data.decode('utf-8'))

            # 如果recv解堵塞，有两种方式 ：
            # 1、客户端发送过来数据
            # 2、客户端调用close，导致了recv解堵塞
            if recv_data :  # 判断发送过来的数据来证明recv解堵塞的原因
                # 回送一部分数据
                new_client_socket.send('hhhhh'.encode('utf-8'))
            else:
                break


        # 关闭套接字，不再为该客户端服务
        new_client_socket.close()
        print('已经为该客户端服务完毕。。。')

    tcp_server_socket.close()




if __name__ == '__main__':
    main()