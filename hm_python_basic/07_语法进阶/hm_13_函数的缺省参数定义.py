def print_info(name, gender=True):

    '''
    假设班上的男生，居多！！！
    :param name: 班上同学的姓名
    :param gender: True  男生   False  女生
    :return:
    '''
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 注意：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小马哥")
print_info("小米", False)


