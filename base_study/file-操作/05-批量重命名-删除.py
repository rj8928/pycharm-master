import os
#1. 获取要重命名的文件夹
folder_name = input("请输入要重命名的文件夹：")
del_name = input("请输入要删除的字符：")
#2. 获取要重命名的文件名
file_name = os.listdir(folder_name)
os.chdir(folder_name)
#print(file_name)  for 测试
#3. 重命名
for name in file_name:
    new_name = name.replace(del_name,"")
    os.rename(name,new_name)
    print(name)
    
