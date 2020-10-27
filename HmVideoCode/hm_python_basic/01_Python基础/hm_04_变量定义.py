# 1、定义一个变量记录QQ号码
qq_number = "1085953194"

# 2、定义一个变量记录qq密码
qq_password = "Zz1085953194"

print(qq_number,qq_password)

"""
需求--超市买苹果：
1、苹果单价8.5元/斤
2、苹果买5斤
3、计算付款金额
4、只要买苹果，就返还5元钱，重新计算付款金额
"""
# 1、定义price变量存储苹果单价
price = 8.5

# 2、定义weight存储苹果斤数
weight = 5

# 3、定义money变量计算付款金额
money = price * weight

# 4、只要买苹果，就返还5元钱，重新计算付款金额
money = money - 5

# 5、在控制台输出付款金额
print(money, price * weight)