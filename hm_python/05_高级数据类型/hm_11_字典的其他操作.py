xiaoming = {"name":"xiaoming",
            "age":18,
            "gender":True,
            "height":1.75}

# 1、统计字典中键值对数量
print(len(xiaoming))

# 2、合并字典
# update方法，如果被合并的字典中，包含已经存在的键值对，会覆盖原有的键值对
xiaoxiaoming = {"weight":180,
                "age":20}
xiaoming.update(xiaoxiaoming)
print(xiaoming)

# 3、清空字典
xiaoming.clear()
print(xiaoming)