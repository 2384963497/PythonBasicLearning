import time

def outerTime(func):
    def innerTimer(*args,**kwargs):
        stratTime=time.time()
        print('-'*30)
        func(*args,**kwargs)
        print('-'*30)
        endTime=time.time()
        return endTime-stratTime
    return innerTimer

#计算n的阶乘
@outerTime
def fun1(n):
    r=1
    for i in range(1,n):
        r*=i
        time.sleep(0.1)
    print('{}的阶乘是:{}\n'.format(n,r))

#计算n~m的整数和
@outerTime
def fun2(n,m):
    if n>m:
        n,m=m,n
    sum=0
    for i in range(n,m):
        sum+=i
        time.sleep(0.01)
    print("{}~{}的所有整数和={}\n".format(n,m,sum))

lastTime=fun1(20)
print("总耗时:{}s".format(lastTime))
lastTime=fun2(1,10)
print("总耗时:{}s".format(lastTime))