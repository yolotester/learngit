'''
需求：
1、从控制台输入要出的拳--石头（1）/ 剪刀（2）/布（3）
2、电脑随机出拳
3、比较胜负
'''
# 注意：导入工具包的语句，放在文件的顶部
# 这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具
import random

# 1、从控制台输入要出的拳--石头（1）/ 剪刀（2）/布（3）
player = int(input("请输入要出的拳头，石头（1）/ 剪刀（2）/布（3）："))

# 2、电脑随机出拳--先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)

# 3、提示出拳信息
print("玩家出的拳头是%d --- 电脑出的拳头是%d"  % (player, computer))

# 4、比较胜负
# 玩家胜利的情况
    # 石头 胜 剪刀
    # 剪刀 胜 布
    # 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利啦")

# 平局
elif player == computer:
    print("心有灵犀啊")

# 电脑胜利的情况
else:
    print("电脑胜利啦")