f = open("1.txt","r")
strs =int( input("请输入想要取出的字数："))
strs_1=f.read(strs)
print(strs_1)
f.close()

