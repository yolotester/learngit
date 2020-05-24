import gevent
import requests



def downloader(img_addr,url):

    req =  requests.get(url)  # 打开网址，返回网址的内容
    img_content = req.read()

    with open(img_addr,'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader,'1.jpg','https://anchorpost.msstatic.com/cdnimage/anchorpost/1003/60/d8fe78247c7229b9be220d6b457e8f_1663_1576234625.jpg?imageview/4/0/w/338/h/190/blur/1%22%20src=%22https://anchorpost.msstatic.com/cdnimage/anchorpost/1003/60/d8fe78247c7229b9be220d6b457e8f_1663_1576234625.jpg?'),
        gevent.spawn(downloader,'2.jpg','http://live-cover.msstatic.com/huyalive/64008017-2377721967-10212238087245791232-34850612-10057-A-0-1/20200524142906.jpg')
    ])

if __name__ == '__main__':
    main()