'''
需求：
1、定义bool型变量，has_ticket表示是否有票
2、定义整形变量knife_length表示刀的长度，单位：厘米
3、首先检查是否有车票，如果有票， 才允许进行安检
4、安检时，需要检查刀的长度，判断是否超过20厘米
    5、如果超过20厘米，提示刀的长度，不允许上车
    6、如果不超过20厘米， 安检通过
7、如果没有车票不允许进门
'''
has_ticket = True
knifi_length = float(input("请输入刀的长度："))
if has_ticket:
    print("车票通过，可以进行安检")
    if knifi_length > 20:
        print("刀的长度为%.2f厘米，不允许上车" % knifi_length)
    else:
        print("恭喜你，通过安检！")
else:
    print("请先买票")