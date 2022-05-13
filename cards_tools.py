
card_list = []


def show_menu():

    print("*" * 50)
    print("欢迎使用【名片管理类系统-鲁东大学】V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("0. 退出系统")
    print("")
    print("*" * 50)


def new_card():
    print("-" * 50)
    print("新增名片")
    # 提示输入
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 定义字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 追加列表
    card_list.append(card_dict)

    # print(card_list)
    print("添加%s的名片成功！" % name_str)


def show_all():
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("暂无名片记录！")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                    card_dict["phone"],
                                    card_dict["qq"],
                                    card_dict["email"]))


def search_card():
    print("-" * 50)
    print("搜索名片")

    find_name = input("请输入搜索姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("%s搜索成功！" % find_name)
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("")
            print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["qq"],
                                      card_dict["email"]))
            # TODO 针对找到的名片执行修改和删除操作
            del_card(card_dict)
            break
    else:
        print("%s查无此人！" % find_name)


def del_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名(回车不修改)：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话(回车不修改)：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ(回车不修改): ")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱(回车不修改)：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典中原有值
    :param tip_message: 输入的提示信息
    :return: 如果输入内容就返回内容，否则返回字典原有值
    """
    # 1.提示输入
    result_str = input(tip_message)
    # 2.判断是否输入内容
    if len(result_str) > 0:
        return result_str
    # 3.如果没有输入，返回字典原有值
    else:
        return dict_value

