class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平方米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具名称列表：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)

        # 1.判断家具的面积
        if item.area > self.free_area:
            print("%s家具太大，放不下，不能添加" % item.name)
            return

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        print("添加家具%s成功" % item.name)

        # 更新剩余面积
        self.free_area -= item.area



# 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 创建房子对象
my_house = House("两室一厅", 100)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)
'''
总结：
主程序只负责创建 房子 对象和 家具 对象
让 房子 对象调用 add_item 方法 将家具添加到房子中
面积计算、剩余面积、家具列表 等处理都被 封装 到 房子类的内部
'''