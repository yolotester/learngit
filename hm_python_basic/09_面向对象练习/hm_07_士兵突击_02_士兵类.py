class Gun:

    def __init__(self, type):

        # 枪的类型
        self.type = type

        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了" % self.type)
            return

        # 2.发射子弹（子弹数量 - 1）
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s]突突突...剩余子弹[%d]" % (self.type, self.bullet_count) )


class Soldier:

    def __init__(self, name):

        # 姓名
        self.name = name

        # 枪 - 新兵没有枪
        self.gun = None

    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun is None:
            print("[%s] 没有枪" % self.name)
            return

        # 2.喊口号
        print("冲啊...[%s]" % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(10)

        # 4.发射子弹
        self.gun.shoot()

# 创建枪对象
ak47 = Gun("AK47")

# 创建士兵对象
xusanduo = Soldier("许三多")

xusanduo.gun = ak47  # 枪类对象 赋值给 士兵类对象的属性，则该属性，可以调用枪类对象的方法和属性
xusanduo.fire()
print(xusanduo.gun)
