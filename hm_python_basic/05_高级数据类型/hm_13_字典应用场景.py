# 使用 多个键值对， 存储 描述一个 物体 的相关信息
# 将 多个字典  放在 一个列表 中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
# 字典 与 列表的结合

student_all = [
            {"name":"xiaoming",
            "age":18,
            "gender":True,
            "height":1.75},
            {"name":"YOlo",
            "age":18,
            "gender":True,
            "height":1.75}

]


for student_info in student_all:
    print("学生信息如下: %s" % student_info)