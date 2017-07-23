try:
    open("xxx.txt")
    print(num)
    print("--1--")
except NameError:
    print("没定义")
except FileNotFoundError:
    print("文件不存在")
print("--2---")
