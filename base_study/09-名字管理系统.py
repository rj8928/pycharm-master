#打印功能提示
print("="*50)
print(" 1:添加一个新名字")
print(" 2:删除一个名字")
print(" 3:修改一个名字")
print(" 4:查询一个名字")
print(" 5:退出程序")
print("="*50)
names = [] #定义一个空列表来存放名字
#获取用户的选择
while True:
    num = int (input("  请输入对应序号："))
    #根据用户的选择。执行相应的功能
    if num == 1:
        print("请输入一个新名字：",end="")
        new_name = input()
        names.append(new_name)
        print("="*50)
        print("添加后的表为")
        print(names)
        print("="*50)
    elif num == 2:
        print("请输入要删除的名字：",end="")
        del_name = input()
        names.remove(del_name)
        print("删除后的表为")
        print(names)
        print("="*50)
    elif num == 3:
        print("请输入要修改的名字")
        change_name = input()
        print("请输入修改后的名字")
        change1_name = input()
        num_0 = names.index(change_name)
        names[num_0]=change1_name
        print("修改后的表为")
        print(names)
        print("="*50)

    elif num == 4:
        find_name = input("请输入要查询的名字：")
        if find_name in names:
            print("该名字在表中")
            print("="*50)
        else:
            print("查无此人")
            print("="*50)
    elif num == 5:
        break
    else:
        print("您的输入有误，请重新输入")
