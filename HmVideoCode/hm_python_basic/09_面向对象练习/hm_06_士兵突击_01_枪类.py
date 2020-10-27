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


ak47 = Gun("AK47")
ak47.add_bullet(10)
ak47.shoot()