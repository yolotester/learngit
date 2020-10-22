class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 标记是否执行过初始化动作 -- 默认为 未执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1、判断类属性是否是空对象
        if cls.instance is None:
            # 2、调用父类方法，为第一个对象分配空间。并用类属性接收
            cls.instance = super().__new__(cls)

        # 3、返回类属性保存的引用，则后面无论创建多少个对象，new方法返回的引用都是这个
        return cls.instance


    def __init__(self):

        # 1、判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 2、如果没有执行过初始化动作，则再执行初始化动作
        print("执行初始化动作的代码")

        # 3、修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个播放器对象
wangyiyun = MusicPlayer()
print(wangyiyun)

qqyinyue = MusicPlayer()
print(qqyinyue)