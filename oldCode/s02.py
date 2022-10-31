from multiprocessing import *
import time
import os
def funcPro2(count):
    for i in range(count):
        # print(name+"在跳舞")
        print("-------进程2正在唱 跳 rap 篮球")
        time.sleep(0.02)
#def funcPro2(**kwargs):
#    for i in range(kwargs['count']):
#        print(kwargs['name']+"在跳舞")
#        print("-------进程2正在唱 跳 rap 篮球")
#        time.sleep(0.02)
if __name__=='__main__':
    # pro2=Process(target=funcPro2,kwargs={"name":"小虎",'count':6})
    #pro2=Process(target=funcPro2,kwargs={"name":"小虎",'count':6,'age':2})
    pro2=Process(target=funcPro2,args=(6,))
    pro2.start()