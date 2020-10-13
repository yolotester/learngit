import socket
import re


def server_response(new_socket):
    '''
        为客户端服务提供数据
        1、先收到客户端的http请求， 格式如： GET / HTTP/1.1     ......
        2、构造返回给客户端的应答数据， 格式如： HTTP/1.1  200 OK    ......
    '''
    # recv()方法1024，表示最大接收1024个字节，返回的是普通数据
    client_request = new_socket.recv(1024).decode('utf-8')
    # print(client_request)  # 调试看客户端请求,数据是字节型数据，需要decode，解码后为字符串

    # 对客户端请求解码后的字符串进行切割
    client_request_line = client_request.splitlines()
    print(client_request_line)

    # re匹配请求的url,格式如：GET /06table.html HTTP/1.1
    ret = re.match(r'[^/]+/([^ ]*)', client_request_line[0])
    file_name = ''  # 如果下面if语句不成立，则file_name变量不存在，需要先定义file_name变量
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if ret == '/':
            file_name = '06table.html'

    try:
        # 发送用户请求的页面
        f = open(r"C:\Users\yolo\Desktop\web\web01" + "\\" + file_name, 'rb')

    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----file not found ----"
        new_socket.send(response.encode('utf-8'))

    else:

        response = "HTTP/1.1 200 OK\r\n"  # python中用\r\n表示换行
        response += "\r\n"
        # 发送固定页面数据
        # response += "<h1>YOLo</h1>"
        html_content = f.read()  # 为字符型数据
        f.close()

        # 发送response header
        new_socket.send(response.encode('utf-8'))
        # 发送response body
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()  # 因为tcp的机制，先关闭的服务器端的close，则有2分钟等待时间保留资源。要么更换端口，或者设定套接字


def main():
    '''
        目标：整体控制http服务器的工作流程
        1、http服务器是基于tcp的，则可套用实现tcp服务器过程
    '''
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设定套接字

    # 绑定端口，ip地址,bind()方法里数据是元祖格式
    tcp_server_socket.bind(('127.0.0.1', 7890))

    # 将套接字变为监听套接字， 128通俗理解为队列里最多只能允许128个客户端连接
    tcp_server_socket.listen(128)  # 操作系统内核维护一个队列，以跟踪这些完成的连接 但服务器进程还没有接手处理或正在进行的连接

    while True:  # 一直为客户端服务

        # 等待客户端的连接请求，返回值是个元祖
        new_socket, client_addr = tcp_server_socket.accept()  # 拆包

        # 为客户端提供数据
        server_response(new_socket)

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
