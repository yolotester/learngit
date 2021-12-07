xiaoming = {"name":"xiaoming",
            "age":18,
            "gender":True,
            "height":1.75}

# 1、取值
print(xiaoming["name"])  # 在取值的时候，如果指定的key不存在，程序会报错！！！
print(xiaoming.get("xxx"))  # 取值的时候，建议使用get方法    返回None

# 2、增加/修改
# 如果key不存在，会新增键值对
xiaoming["weight"] = 180
# 如果key存在，会修改已经存在的键值对
xiaoming["name"] = "xiaoxiaoming"

# 3、删除
xiaoming.pop("age")

# 在删除键值对的时候，如果指定的key不存在，程序会报错
# xiaoming.pop("agggg")  # KeyError: 'agggg'

print(xiaoming)