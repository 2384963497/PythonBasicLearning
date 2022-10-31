from multiprocessing import *
import time
import os
from tkinter.tix import Tree

def func(n):
    for i in range(n):
        print(f"子进程还有{n: ^5}秒后结束")
        time.sleep(1)
        n-=1

if __name__=='__main__':
    subpor=Process(target=func,args=(10,))
    subpor.daemon=True
    subpor.start()
    for i in range(4):
        print("父进程在执行！！！！！！！！")
        time.sleep(1)
    print("父进程结束！！！！！！！！！！！"*3)
