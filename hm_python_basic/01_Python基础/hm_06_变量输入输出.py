'''
需求--买苹果增强版1：苹果的单价 和 重量 需要输入的时候。
'''
# 1、输入苹果的单价
price_str = input("苹果的单价：")

# 2、输入苹果的重量
weight_str = input("苹果的重量：")

# 注意：两个字符串变量之间不能直接使用乘法
# money = price_str * weight_str
# 需要进行类型转换
# 1、将单价转换为小数
price = float(price_str)

# 2、将重量转换为小数
weight = float(weight_str)

# 3、计算支付的金额
money = price * weight

print(money)


'''
需求--买苹果增强版2：苹果的单价 和 重量 需要输入的时候。
'''
# 1、输入苹果的单价 并转换
price = float(input("苹果的单价："))

# 2、输入苹果的重量 并转换
weight = float(input("苹果的重量："))

# 3、计算支付的金额
money = price * weight

print(money)