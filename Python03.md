# Python03

[toc]



---

##闭包和装饰器:car:

*   Python中变量的**作用域**是根据函数划分的

    *   LEGB
        *   Local
        *   Enclosing
        *   Global
        *   Built-in

*   内层函数可以逐级访问外层函数中的变量

*   如果内层函数要修改外层函数的变量则要加上nonlocal n

*   如果要修改全局变量的值则要加上global n

*   闭包和修饰器的基本结构

    *   ```python
        def loginRequired(func):
            def check(*args,**kwargs):
                if loginFlag==True:
                    func(*args,**kwargs)
                else:
                    print("用户未登录请登录后再试")
                    print("选择完成(2s后返回)")
                    time.sleep(2)
            return check
        ```

*   当一个函数挂了一个装饰器后，会自动执行一次外层函数

*   函数名也是一个变量可以被改变

*   **闭包基本格式：**

    *   函数嵌套定义函数

    *   内层函数使用外层函数的变量

    *   外层函数返回内层函数的函数名(即内层函数地址)

*   装饰器实例

    *   ```python
        import time
        
        #########################################################################
        #############################关键代码######################################
        def outerTime(func):
            def innerTimer(*args,**kwargs):
                stratTime=time.time()
                print('-'*30)
                func(*args,**kwargs)
                print('-'*30)
                endTime=time.time()
                return endTime-stratTime
            return innerTimer
        #########################################################################
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
        ```

---

## 匿名函数lambda

*   格式

    *   lambda 参数列表:返回值

*   实例

    *   ```python
        l1=[
            {'name':'xiaohu','damage':2200},
            {'name':'Tian','damage':4397},
            {'name':'clearLove','damage':4396},
            {'name':'kid','damage':443},
            ]
        
        
        lam=lambda x:x['damage']
        
        lMax=max(l1,key=lam)
        # lMax=max(l1,key=lam)
        for i in l1:
            if lam(i)>2200:
                print(i['name'])
        ```

*   一般将lambda 函数作为函数参数使用

---

## map()

*   格式

    *   map(fun,...)
        *   第一个参数要是一个函数的名称，**后面的若干个值要为可迭代的**

*   实例

    ```python
    r=list(map(lambda x,y:x+y,range(1,6),range(1,6))) #[2, 4, 6, 8, 10]
    r=list(map(str,range(1,3)))	#['1', '2']
    r=list(map(lambda x,y:str(x)+str(y),range(1,7),range(100,601,100)))#['11', '22', '33', '44', '55', '66']
    ```

---

## reduce()

*   格式

    *   reduce()包含在functools库
    *   reduce(fun,sep[,inital])
        *   fun是必须两个参数的函数，后面是一个可迭代的对象,inital是指定最初的值

*   实例

    *   ```python
        from functools import reduce
        
        l1=[1,2,3,4,5,6,7,8,9,10]
        r=reduce(lambda x,y:x+y,l1)
        #r=reduce(lambda x,y:x+y,l1,10)  l1后面的时代表 一开始的值 
        print(r)#55
        ```

---

## filter()

*   格式

    *   filter(func,sep)

*   实例

    *   ```python
        l1=[
            {'name':'xiaohu','damage':2200},
            {'name':'Tian','damage':4397},
            {'name':'clearLove','damage':4396},
            {'name':'kid','damage':443},
            ]
        l1 = filter(lambda x:x['damage']>2200,l1)
        print(list(l1))#[{'name': 'Tian', 'damage': 4397}, {'name': 'clearLove', 'damage': 4396}]
        ```

*   将符合func函数的迭代元素保留

---

## isinstance()

*   isinstance(val,type)

*   返回val是否为type类型

*   ```python
    print(isinstance(23,int))
    #True
    ```

---

## 文件操作

*   打开文件

    *   ```python
        #格式1
        mytxt=open(r"D:\002MyCode\Python\aim.txt",'r')
        
        #格式2
        with open(r"D:\002MyCode\Python\aim.txt",'r') as mytxt:
        	pass
        
        #格式2可以自动释放资源
        ```

        *   选择打开文件的方式
            *   "r"读 	;"w"写 	;"rb"二进制读 	;"a"追加

*   关闭文件
    *   mytxt.close()

*   读取

    *   mytxt.read()
    *   mytxt.readline()
        *   读一行文本在末尾加上换行符'\n'，最后一行不加
    *   mytxt.readlines()
        *   读取所有内容，并且将每行作为一个元素，最后组成一个列表返回
        *   读多行文本在每行末尾加上换行符'\n'，最后一行不加

*   写入

    *   mytxt.write()
    *   mytxt.writeline()
        *   可以写入列表、元组等类型的数据


---

## OS:car:

*   os.path.
    *   os.path.dirname(\__file__)
        *   返回当前文件夹路径 str类型
    *   os.path.join(path,file)
        *   将文件名和路径拼接并返回 str类型
        *   可以拼接多个

    *   os.path.isabs(path)

        *   返回path是否为绝对路径

    *   os.path.abspath(path)

        *   将path转为绝对路径

    *   os.getcwd()

        *   返回当前文件目录绝对位置
        *   os.path.dirname(\__file__) 返回当前文件绝对路径

    *   os.path.split(path)

        *   返回一个元组，第一个元素为文件目录，第二个元素为文件名和拓展名

        *   ```python
            p=os.path.abspath("../turtleAndRabit/p2.jpeg")   	 	#False
            print(os.path.isabs("../turtleAndRabit/p2.jpeg")) 		
            print(os.path.split(p))		#('D:\\turtleAndRabit', 'p2.jpeg')
            ```

    *   os.path.splittext(path)

        *   返回一个元组，第一个元素为文件所在位置，第二个元素为文件拓展名 

        *   ```python
            p=os.path.abspath("../turtleAndRabit/p2.jpeg")
            print(os.path.splitext(p))#('D:\\turtleAndRabit\\p2', '.jpeg')用于判断文件类型
            ```

    *   os.path.getsize(path)

        *   返回文件大小，单位字节

    *   os.path.isdir(path)

        *   是否为文件夹

    *   os.path.exists(path)

        *   返回文件是否存在

*   实例:复制文件

    *   ```python
        import os
        #E:\荐片
        #F:\right
        sourceDir=input("请输入源文件的路径:")
        targetDir=input("请输入目标文件的路径:")
        
        def copyDir(sDir,tDIr):
            fList=os.listdir(sDir)
            for i in fList:
                tempFile=os.path.join(sDir,i)
                if os.path.isdir(tempFile):
                    newDir=os.path.join(tDIr,i)
                    os.mkdir(newDir)
                    copyDir(tempFile,newDir)
                else:
                    with open(tempFile,"rb") as rsteam:
                        temp=rsteam.read()
                    with open(os.path.join(tDIr,i),"wb") as rstream:
                        rstream.write(temp)
            print("复制完成")
        
        copyDir(sourceDir,targetDir)
        ```


*   os.listdir(path)
    *   返回一个列表，别表中为path文件夹下的所有文件名+后缀
*   os.mkdir(path)
    *   创建一个文件夹
    *   已存在，则报错
*   os.rmdir(path)
    *   移除一个文件夹
    *   只能删除空文件夹
*   os.chdir(path)
    *   可以改变当前目录
    *   默认当前目录是文件所在目录

---

## 异常处理:car:

*   格式

    *   ```python
        try:
        	<语句>        #运行的代码
        except <名字>：
        	<语句>        #如果在try部份引发了'name'异常
        except <名字>，<数据>:
        	<语句>        #如果引发了'name'异常，获得附加的数据
        except exception as name:
                #可以引用引起问题的错误代码name
        else:
        	<语句>        #如果没有异常发生
        ```

    *   ```python
        try:
        	<语句>
        except:
        	...
        finally:
        	<语句>    #退出try时总会执行
        raise
        ```

        *   在try结束后总后执行finally内的语句；即便在try中有return也会执行finally；且如果finally中也有return val则会把前面的返回值覆盖

    *   ```python
        except <名字>，<数据>:
        	<语句>        #如果引发了'name'异常，获得附加的数据
        ```

        *   ```python
            # 定义函数
            def temp_convert(var):
                try:
                    return int(var)
                except ValueError, Argument:
                    print "参数没有包含数字\n", Argument
            
            # 调用函数
            temp_convert("xyz")
            
            '''
            $ python test.py 
            参数没有包含数字
            invalid literal for int() with base 10: 'xyz'
            '''
            ```

    *   自定义异常arise

        *   ```python
            def checkPw(pw):
                if len(pw)<8:
                    raise Exception("密码至少8位!!!")
                else:
                    return 1
            
            pw="1236s7"
            
            try:
                checkPw(pw)
            except Exception as err:
                print(err)
            else:
                print("密码符合条件")
            
            ```

---

## 推导式

###列表

*   基本格式

    *   list=[新元素表达式 for 迭代对象 in 可迭代对象 [...]]

    *   ```python
        names=["pdd","add","XIAOHU","uzi","Wei","Tian"]
        #######################重要部分##########################
        names=[name for name in names if len(name)<=3]
        print(f"处理一次后为:{names=}")
        #######################重要部分##########################
        names=[name.capitalize() for name in names]
        print(f"处理两次后为:{names=}")
        '''
        处理一次后为:names=['pdd', 'add', 'uzi', 'Wei']
        处理两次后为:names=['Pdd', 'Add', 'Uzi', 'Wei']
        '''	
        ```

*   多个变量的值

    *   ```python
        #输出有元组组成的列表，元组元素的第一个元素是偶数，第二个元素的奇数 0<=x,y<=5
        #[(偶数,奇数),(偶数,奇数),(偶数,奇数)....]
        #######################重要部分##########################
        num=[(x,y) for x in range(6) for y in range(6) if (x%2==0 and y%2==1)]
        print(f"所得到的列表为:{num=}")
        #所得到的列表为:num=[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]
        ```
        

### 集合推导式

+   格式和用法同列表推导式；不同的是集合推导式是用花括号包裹；并且它和集合一样具有去重的功能

### 字典推导式

+   用法同列表推导式

    +   ```python
        #利用字典推导式 交换字典中的key和value
        
        x={'name':'小虎','score':2200,'pos':'mid','age':2200}
        
        x={val:key for key,val in x.items()}
        print(f"处理后的x为{x}")
        ```

    +   返回值的表达式  需要以键值对的方式放入

---

## 生成器

-   定义生成器

    -   name=(表达式 for 迭代对象 in 可迭代对象)

-   使用生成器

    -   name.\__next__()
    -   next(name)
    -   不能超过生成的上届

-   小实例

    -   ```python
        #生成一个2的0次方 到 2的n次方的列表并输出
        
        n=int(input("请输入所求列表的长度:"))
        gener=(2**x for x in range(100000))
        numList=[]
        for i in range(n):
            numList.append(next(gener))
        print(f"生成的列表为:{numList}")
        ```

-   函数中的yield

    -   作用相当于return 表达式 并保存当前函数的位置和状态

-   genratot.send()

    -   在生成器函数暂停处重新执行时，向该处发送一个值


---

## 迭代器

*   迭代器是从集合的第一个元素开始访问，并且能用next()调用下一个值，迭代器只能前进不能后退
*   列表、元组都不是迭代器；但是可以通过iter(name)将可迭代对象转换为迭代器

---

## 单词

*   decorate  装饰
*   wrapper  包装
*   enclosing  嵌套的
*   recursion  递归

-   subscriptable  

-   yield  产生