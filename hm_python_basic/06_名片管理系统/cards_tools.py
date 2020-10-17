cards_list = []

def show_menu():

    '''显示菜单'''
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    '''新增名片'''
    print("-" * 50)
    print("新增名片")

    # 提示用户输入相关名片信息
    name_str = input("请输入名字：")
    QQ_str = input("请输入QQ：")
    email_str = input("请输入Email：")


    # 将用户输入的名片信息定义为 名片字典
    card_dict = {"name":name_str,
                 "QQ":QQ_str,
                 "email":email_str}

    # 将 名片字典 添加到列表中
    cards_list.append(card_dict)
    print(cards_list)

    # 提示用户名片添加成功
    print("添加 %s 的名片成功" % name_str)


def show_all():

    '''显示所有名片'''
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(cards_list) == 0:
        print("当前没有任何名片记录，请先新增名片！")

        # return可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不返回任何结果
        return

    def print_table():
        # 打印表头
        for name in ["姓名", "QQ", "Email"]:
            print(name, end="\t\t")

        print("")

        # 打印分隔线
        print("=" * 50)

    print_table()

    # 遍历名片列表，依次输出列表信息
    for card_info in cards_list:
        print("%s\t\t%s\t\t%s" % (card_info["name"],
                                  card_info["QQ"],
                                  card_info["email"]))


def search_card():

    '''显示所有名片'''
    print("-" * 50)
    print("搜索名片")

    # 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 遍历名片列表，查询要搜索的姓名，如果没有找到，则提示用户
    for card_dict in cards_list:

        if card_dict["name"] == find_name:
            print("姓名\t\tQQ\t\tEmail")
            print("=" * 50)

            # print("")
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["QQ"],
                                      card_dict["email"]))

            # 针对找到的名片记录执行修改和删除的操作
            # 分析：修改和删除的操作 -- 都是针对找到的名片记录
            # 可以对修改和删除的操作 重新封装一个函数，传参找到的名片字典card_dict
            # 这样对阅读代码或者编写代码都更清晰
            deal_card_dict(card_dict)

            break


    else:
        print("抱歉没有找到%s" % find_name)


def deal_card_dict(find_dict):
    '''
    处理查找到的名片
    :param find_dict: 查找到的名片记录
    :return: 无返回
    '''

    print(find_dict)
    action_str = input("请输入您要选择的操作"
                        "[1] 修改 [2] 删除 [0] 返回上级菜单:")

    if action_str == "1":

        find_dict["name"] = input_card_list(find_dict["name"], "姓名：")
        find_dict["QQ"] = input_card_list(find_dict["QQ"], "QQ:")
        find_dict["Email"] = input_card_list(find_dict["email"], "Email:")
        print("修改名片成功！")

    if action_str == "2":

        cards_list.remove(find_dict)
        print("删除名片成功！")


def input_card_list(dict_value, tip_message):

    '''
    修改名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则，返回字典中原有的值
    '''

    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.如果用户输入了，就把用户输入的结果 返回
    if len(result_str) > 0:
        return result_str

    # 3.若用户没有输入，就返回 字典原有的值
    else:
        return dict_value




