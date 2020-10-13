'''
	目标：掌握进程、线程、协程核心代码实现http服务器
'''
import socket
import re
import multiprocessing
import threading
import gevent
from gevent import monkey

monkey.patch_all()


def for_client_service(new_socket):
    '''
        实现为客户端服务的内容
        1.先收到客户端的请求，格式为：GET / HTTP/1.1   空行  body
            1.1 解析客户端请求的页面地址
                1.1.1 收到客户端的请求为字节型数据，需要解码为字符型数据
                1.1.2 对客户端请求（字符串）进行以行分割
                1.1.3 对分割后的数据，进行re匹配出页面地址
        2.构造响应数据，格式为：HTTP/1.1 200 OK  空行  body
            2.1 打开所有html页面的文件
            2.2 在文件夹中匹配客户端请求的页面地址
                2.2.1 若匹配到则返回数据
                2.2.2 若匹配不到则返回错误提示信息
        3.发送服务器响应数据
    '''
    client_request = new_socket.recv(1024).decode('utf-8')
    client_request_line_data = client_request.splitlines()
    print(client_request_line_data)
    ret = re.match(r'[^/]+/([^ ]*)', client_request_line_data[0])

    file_name = ''
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if ret == '/':
            file_name == '06table.html'

    try:
        f = open('./web01/' + file_name, 'rb')
    except:
        server_response = "HTTP/1.1 404 NOT FOUND\r\n"
        server_response += "\r\n"
        server_response += "----File Not Found----"

        new_socket.send(server_response.encode('utf-8'))

    else:
        server_response = "HTTP/1.1 200 OK\r\n"
        server_response += "\r\n"
        html_content = f.read()
        f.close()

        # 字符型和字节型数据不能同时传输，则分别发送响应头和响应体
        new_socket.send(server_response.encode('utf-8'))
        new_socket.send(html_content)

    new_socket.close()


def main():
    '''
        控制整体，http服务器创建步骤
    '''
    # 创建tcp套接字
    http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设定套接字

    # 绑定端口，数据类型为元祖
    http_server_socket.bind(('127.0.0.1', 7890))

    # 将套接字设定为监听套接字
    http_server_socket.listen(128)

    while True:
        # 默认阻塞状态，等待客户端的连接,返回值是一个元祖，则需要拆包
        new_socket, client_addr = http_server_socket.accept()

        # 为客户端进行服务
        # for_client_service(new_socket)

        # 多进程的方式为客户端服务
        p = multiprocessing.Process(target=for_client_service, args=(new_socket,))
        p.start()

        new_socket.close()

    # 关闭套接字
    http_server_socket.close()


if __name__ == '__main__':
    main()