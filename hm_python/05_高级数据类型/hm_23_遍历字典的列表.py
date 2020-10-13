'''
需求：要判断 某一个字典中 是否 存在指定的值
1、如果 存在， 提示并且退出循环
2、如果 不存在， 在循环整体结束 后，希望得到一个统一的提示
'''
name = [
    {"name":"Yolo"},
    {"name":"YYYY"}
]

find_name = "Yol"
for name_info in name:
    print(name_info)

    if name_info["name"] == find_name:
        print("找到了 %s" % find_name)

        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break

    # if - else每次判断如果不成立，else缩进代码都会被执行
    # else:
    #     print("抱歉没找到 %s" % find_name)

# for - else，是循环结束后，才会执行else缩进代码
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现搜索的目标
    # 还希望得到一个统一的提示
    print("抱歉没找到 %s" % find_name)

print("循环结束！")

