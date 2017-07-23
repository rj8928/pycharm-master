import os
from multiprocessing import Pool,Manager

def copyFileTask(fileName,oldFolderName,newFolderName,queue):
    #完成拷贝文件的功能
    fr = open(oldFolderName+"/"+fileName)
    fw = open(newFolderName+"/"+fileName,"w")

    content = fr.read()
    fw.write(content)
    queue.put(fileName)
    fr.close()
    fw.close()

def main():

    #0. 获取要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字:")
    #1. 创建一个文件夹
    newFolderName = oldFolderName+"复件"
    print(newFolderName)
    os.mkdir(newFolderName)
    #2. 获取old文件夹中所有文件的名字
    oldFileList = os.listdir(oldFolderName)
    #3. 使用多进程的方式copy原文件中的数据

    pool = Pool(5)
    queue = Manager().Queue()

    for fileName in oldFileList:
        pool.apply_async(copyFileTask,args=(fileName,oldFolderName,newFolderName,queue))
    num = 0
    aLLNum = len(oldFolderName)
    while True:
        queue.get()
        num +=1
        coptRate = num/aLLNum
        print("\r进度是：%.2f%%"%(coptRate*100),end="")
        if coptRate==1:
            break

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
