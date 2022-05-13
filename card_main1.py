import cards_tools1


while True:
    # TODO(wzx) 显示功能菜单
    cards_tools1.show_menu()
    action_str = input("请输入希望执行的操作：")
    print("您选择的是【%s】" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools1.new_card()
        elif action_str == "2":
            cards_tools1.show_all()
        elif action_str == "3":
            cards_tools1.search_card()
    elif action_str == "0":
        print("欢迎再次使用！")
        break
    else:
        print("您输入的不正确，请重新请选择！")