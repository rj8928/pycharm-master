names = input("请输入要复制的文件名：")
f= open(names,"r")
new_name ="new"+names
cp = open(new_name,"a")
while True:
    r_temp = f.read(1024)
    cp.write(r_temp)
    if r_temp !="":
        break
f.close()
cp.close()
    
