import os
#1. 获取要重名名的文件夹
folder_name = input("请输入要重命名的文件夹：")
#2. 获取指定的文件夹中的所有名字
file_names = os.listdir(folder_name)
#3. 重命名
os.chdir(folder_name)
for name in file_names:
    print(name)
    
    os.rename(name,"qwer"+name)

