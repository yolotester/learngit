# 文件下载server
from socket import *


def send_flle_2_client(new_client_socket,client_addr):
    # 接收客户端发送的要下载的文件名字
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端（%s）要下载的文件是：%s' % (str(client_addr)), file_name)  # 打印调试信息

    file_content = None
    # 打开这个文件，读取数据
    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件（%s）' % file_content)



    # 发送这个文件的数据到客户端
    if file_content:
        # new_client_socket.send('hahhahahha'.encode('utf-8'))
        new_client_socket.send(file_content)

def main():

    # 创建套接字
    server_socket = socket(AF_INET,SOCK_STREAM)

    # 绑定服务器ip和port信息
    server_ip = input('请输入要绑定的服务器的IP：')
    server_port = int(input('请输入要绑定的服务器的port：'))
    server_socket.bind((server_ip,server_port))

    # 创建监听套接字
    server_socket.listen(128)

    # 循环为多个客户端服务
    while True:

        # 等待客户端连接,返回的是一个元组（新的套接字，客户端信息）
        new_client_socket,client_addr = server_socket.accept()

        # 调用发送文件服务，完成为客户端服务
        send_flle_2_client(new_client_socket,client_addr)


        # 关闭套接字
        new_client_socket.close()

    server_socket.close()

if __name__ == '__main__':
    main()

