class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平方米" % (self.name, self.area)


# 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print("这是一个%s" % bed)
print(chest)
print(table)