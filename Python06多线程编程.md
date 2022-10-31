# Python06多线程编程

[toc]

---

# 多任务

-   并发
    -   多个任务交替执行
-   并行
    -   多个任务同时执行；单核无法实现

## 多线程





---

## 多进程

-   在主进程中创建若干个子进程；并使他们**同时执行**

-   获取进程的编号`os.getpid()`；获取父进程的编号`os.getppid()`

-   python中实现多进程的基本三个步骤
    1.   导入多进程包`import multiprocessing`
    2.   创建一个子进程对象 `arg=multiprocessing.Porsess(target=funcName,name=proseccName)`
    3.   启用进程任务`arg.start()`

-   实例1

    -   ```python
        from multiprocessing import *
        import time
        
        def funcPro1():
            for i in range(200):
                print("----------------------进程1正在丛林里面抢肉吃")
                time.sleep(0.02)
        def funcPro2():
            for i in range(200):
                print("-------进程2正在唱 跳 rap 篮球")
                time.sleep(0.02)
        if __name__=='__main__':
            pro1=Process(target=funcPro1)
            pro2=Process(target=funcPro2)
            print("=================主线程输出开始=====================")
            pro1.start()
            pro2.start()
            for i in range(20):
                print("主进程在运行...")
                time.sleep(0.1)
            print("=================主线程输出完咯=====================")
        ```

-   实例2(带有元组)

    -   ```python
        def funcPro1(n):
            for i in range(n):
                print("----------------------进程1正在丛林里面抢肉吃")
                time.sleep(0.02)
        
        pro1=Process(target=funcPro1,args=(100，))
        ```

-   实例3(参数为字典)

    -   ```python
        def funcPro2(count, name):
            for i in range(count):
                print(name+"在跳舞")
                print("-------进程2正在唱 跳 rap 篮球")
                time.sleep(0.02)
        #def funcPro2(**kwargs):
        #    for i in range(kwargs['count']):
        #        print(kwargs['name']+"在跳舞")
        #        print("-------进程2正在唱 跳 rap 篮球")
        #        time.sleep(0.02)
        if __name__=='__main__':
            pro2=Process(target=funcPro2,kwargs={"name":"小虎",'count':6})
            #pro2=Process(target=funcPro2,kwargs={"name":"小虎",'count':6,'age':2})
            pro2.start()
        ```

    -   用名称进行匹配或者传入整个字典


-   父进程会等所有子进程结束后再结束

-   将子进程设置为守护子进程；使父进程代码结束后结束自己

    -   `subpor.daemon=True`需要写在`subpor.start()`之前

    -   ```python
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
        ```

---

## 单词

-   daemon  守护子进程
-   thread  线;线程
