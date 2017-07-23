import os
import time
ret = os.fork()
if ret == 0:
        print("--1--")
        #time.sleep(1)
else:
        print("--2--")
        #time.sleep(1)
ret = os.fork()
if ret == 0:
        print("--3--")
        #time.sleep(1)
else:
        print("--4--")
        #time.sleep(1)
    
