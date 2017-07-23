import os
import time
ret = os.fork()
print(ret)
#if ret == 0:
#    while True:
#        print("--1--")
#        time.sleep(1)
#else:
#    while True:
#        print("--2--")
#        time.sleep(1)
    
if ret > 0:
    print("父进程%d"%os.getpid())
else:
    print("子进程%d  父进程%d"%(os.getpid(),os.getppid()))
