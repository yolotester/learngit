# 文件下载client
from socket import *


def main():

    # 创建套接字
    client_socket = socket(AF_INET,SOCK_STREAM)

    # 连接服务器
    # 获取服务器的ip和port
    server_ip = input('请输入服务器的IP：')
    server_port = int(input('请输入服务器的port：'))
    server_addr = (server_ip,server_port)
    client_socket.connect(server_addr)

    # 获取要下载的文件名
    download_file_name = input('请输入要下载的文件名字：')

    # 将文件名发送给服务器
    client_socket.send(download_file_name.encode('utf-8'))

    # 接收文件中的数据
    recv_data = client_socket.recv(1024*1024)  # 1024=1k 1024*1024=1M

    # 服务器返回数据后保存到一个文件中
    # 判断服务器是否返回有数据,有数据再写入文件中
    if recv_data:
        with open('[新]'  + download_file_name ,'wb') as f :
            f.write()


    # 关闭套接字
    client_socket.close()


if __name__ == '__main__':
    main()