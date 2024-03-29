class MusicPlayer(object):


    def __new__(cls, *args, **kwargs):

        # 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 为对象分配空间，该方法为静态方法，需要主动传递参数
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建一个播放器对象
wangyiyun = MusicPlayer()
print(wangyiyun)