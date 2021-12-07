import socket


def server_response(new_socket):
    '''
        为客户端服务提供数据
        1、先收到客户端的http请求， 格式如： GET / HTTP/1.1     ......
        2、构造返回给客户端的应答数据， 格式如： HTTP/1.1  200 OK    ......
    '''
    client_request = new_socket.recv(1024)
    print(client_request)  # 调试看客户端请求

    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "<h1>hahahah</h1>"

    # send()方法只能发送字节型数据即b''这种
    new_socket.send(response.encode('utf-8'))


def main():
    '''
        目标：整体控制http服务器的工作流程
        1、http服务器是基于tcp的，则可套用实现tcp服务器过程
    '''
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口，ip地址,bind()方法里数据是元祖格式
    tcp_server_socket.bind(('127.0.0.1', 7890))

    # 将套接字变为监听套接字
    tcp_server_socket.listen(128)

    while True:  # 一直为客户端服务

        # 等待客户端的连接请求，返回值是个元祖
        new_socket, client_addr = tcp_server_socket.accept()  # 拆包

        # 为客户端提供数据
        server_response(new_socket)

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
