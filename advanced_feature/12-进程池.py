from multiprocessing import Pool
import os
import random
import time
def worker(num):
    for i in range(random.randint(1,3)):
        print("--%d-%d-"%(i,num))

pool = Pool(3)

for i in range(10):
    print("--%d--"%i)
    pool.apply_async(worker,(i,))

pool.close()
pool.join()
