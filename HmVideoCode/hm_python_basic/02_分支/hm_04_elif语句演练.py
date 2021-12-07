'''
需求：定义holiday_name字符串变量记录节日名称
1、如果是情人节， 应该 买玫瑰花 或 看电影
2、如果是平安夜， 应该 买苹果 或 吃大餐
3、如果是生日， 应该 买蛋糕
4、其他的日子每天都是节日啊......
'''
holiday_name = input("今天是什么日子：")

if holiday_name == "情人节":
    print("今天买玫瑰花")
    print("今天看电影")
elif holiday_name == "平安夜":
    print("今天吃苹果")
elif holiday_name == "生日":
    print("今天吃蛋糕")
else:
    print("每天都是节日，每天都吃好吃的！")


