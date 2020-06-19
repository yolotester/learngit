import socket


def send_msg(udp_socket):
    '''发送消息'''

    # 绑定对方地址信息和输入发送的数据
    dest_ip = input('请输入对方的IP：')
    dest_port = int(input('请输入对方的端口号:'))
    send_data = input('请输入要发送的内容：')
    # 发送数据
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))

def recv_msg(udp_socket):
    '''接收数据'''

    recv_data = udp_socket.recvfrom(1024)
    print('%s:%s' % (str(recv_data[1]), recv_data[0].decode('utf-8')))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.DGRAM)

    # 绑定自己的地址信息
    udp_socket.bind('',7777)

    # 循环处理事情
    while True:
        print('=========yolo chat room=========')
        print('1:发送功能')
        print('2:接收功能')
        print('0:退出系统')

        op = input('请输入功能：')
        if op == '1':
            # 发送数据
            send_msg(udp_socket)
        elif op == '2':
            # 接收数据
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print('请重新输入.....')


    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()