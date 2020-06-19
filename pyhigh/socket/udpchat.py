
from socket import *


def main():
    # 创建套接字,可以同时收发数据
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    # 绑定自己本地的地址信息
    local_addr = ('',7788)
    udp_socket.bind(local_addr)

    # 绑定对方地址信息
    dest_ip = input('请输入对方的IP：')
    try:
        dest_port = int(input('请输入对方的端口号：'))  # 需要是int数据，input是str数据，需要int转换数据,用户输入数据不靠谱，需要捕获异常
    except Exception as e:
        print('请输入数字：',str(e) )



    # 从键盘获取数据
    send_data = input('请输入要发送的数据：')  # 需要的是bytes数据，input是str数据，需要编码成bytes数据

    # 发送数据
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

    # 接收数据
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]
    send_addr = recv_data[1]
    print('%s : %s' % (str(send_addr),recv_msg.decode('utf-8')))

    # 关闭套接字
    udp_socket.close()




if __name__ == '__main__':
    main()