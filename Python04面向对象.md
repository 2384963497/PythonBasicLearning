# Python04

 

## 类

-   创建类

    -   ```python
        class ClassName:
           '类的帮助信息'   #类文档字符串
           class_suite  #类体
        '''
        class_suite 由类成员，方法，数据属性组成。
        '''
        ```

    -   类名遵循大驼峰命名法

-   类属性和对象属性

    -   类属性

        -   在创建类时设置的默认属性

    -   对象属性

        -   在创建完成类对象后所赋予的属性
        -   对象属性是动态创建的

    -   如果访问一个类对象属性，但是该属性没有赋值；则会使用类属性

        -   ```python
            class Student():
                name="XiaoMing"
                score=777
            
            Xh=Student()
            Xh.name="小虎"
            
            print(Xh.name,Xh.score)
            '''
            小虎 777
            '''
            ```

-   使用类

    -   格式

        -   ```python
            name=ClassName()
            -   当创建对象后；则会再内存中开辟一块空间给类对象
            ```
    
-   类对象可以和普通变量一样赋值；被赋值的变量指向类对象的地址




## 方法

-   方法可以理解为类中特有的函数，其用法和函数大致一样

-   一个类中有多个同名方法；则会覆盖前面的类

-   方法中可以嵌套调用其他方法

    -   ```python
        def showInfo(self):
               	...
                self.showName()
        ```

-   实例方法(对象方法、普通方法)

    -   ```python
        def showInfo(self):
                print(f"姓名:{self.name},分数:{self.score}")
        ```

-   魔术方法

    -   普通的方法必须要调用才会生效；但魔术方法是达成某种条件就能自动触发的方法

    -   def  \__init__(self)

        -   创建对象时执行的方法；用于初始化类对象的属性

        -   ```python
            def __init__(self):#__name__
                    pass
            ```

    -   def \__call__(self)

        -   可以用调用函数的方法调用call方法; 类名()

        -   ```python
            class Student():
                def __init__(self):
                    name=None
                def __call__(self, *args, **kwds):
                    print(f"姓名:{self.name}")
            
            Xh=Student()
            Xh.name="xiaohu"
            Xh()
            #姓名:xiaohu
            ```

    -   def \__str__(self)

        -   不适用该方法之前，打印一个类对象；只会打印对象的地址

        -   重写\__str__方法后可以指定返回的内容

        -   一定要在方法中添加return

        -   ```python
            class Book:
                def __init__(self) -> None:
                    self.name=None
                    self.price=None
                def __str__(self):
                    return (f"书本的名称为:{self.name}\n价格为:{self.price}")
            
            itake=Book()
            itake.name="Python零基础到项目实战"
            itake.price=86
            temp=itake
            print(temp.name)
            print(itake)
            '''
            Python零基础到项目实战
            书本的名称为:Python零基础到项目实战
            价格为:86
            '''
            ```

-   类方法

    -   ```python
        @classmethod
        def showCount(cls):
                print(f"姓名:{cls.name},分数:{cls.score}")
        ```

    -   cls即clas的缩写，也可以该成其他合法标识符

    -   类方法使用的属性是类的属性

    -   类方法中也可以使用普通方法

    -   一般是用类方法；只要使用它不依赖与类对象的特点

    -   ```python
        class Student():
            studentCount=0
            name="XiaoMing"
            score=777
        
            def __init__(self) -> None:
                Student.studentCount+=1
            ##############################################################
            @classmethod
            def showTatal(cls):
                print(f"一共有{cls.studentCount}名学生录入了信息")
            ##############################################################
        Student.showTatal()
        Xh=Student()
        Xh.name="小虎"
        XM=Student()
        Uzi=Student()
        Mark=Student()
        Student.showTatal()
        #一共有0名学生录入了信息
        #一共有4名学生录入了信息
        ```
    
-   静态方法

    -   需要@staticmethod装饰器
    -   静态方法可以不传递参数
    -   只能访问类方法

## 私有化

-   在类属性前加上__则会将该属性定义为私有的属性；即只能在类的内部才能查看和修改；外界无法查看和修改

-   私有化的优势

    -   隐藏内部数据，提高安全性
    -   在输入和输出时；通过方法修改和输出提高数据一致性

-   私有化下的数据修改和输出

    -   ```python
      class Std:
            def __init__(self,name,score) -> None:
              self.__name=name
              self.__score=score
          
          def setScore(self,newscore):
              if isinstance(newscore,int) or isinstance(newscore,float):
                  self.__score=newscore
              else:
                  print("类型错误！")
          def getName(self):
              return self.__name
          def getScore(self):
              return self.__score
      
      clearLove=Std("厂长",2200)
      print(f"名字为:{clearLove.getName()},分数为:{clearLove.getScore()}")
      clearLove.setScore('4396')
      print(f"名字为:{clearLove.getName()},分数为:{clearLove.getScore()}")
      ```
      
    -    私有化的底层其实是将`__name`改写成为了`_Std__name`;即可以用强行访问`_Std__name`强行访问但不建议
    
    -    通过`@property` 装饰器实现私有变量的快捷访问和修改
    
         -    ```python
              class Std:
                  ...
              
                  @property
                  def name(self):
                      return self.__name
              
                  @name.setter
                  def name(self,temp):
                      self.__name=temp
              
                  @property
                  def score(self):
                      return self.__score
                  ...
              
              ...
              print(f"名字为:{clearLove.name},分数为:{clearLove.score}")
              clearLove.name="明凯"
              ...
              
              ```
    
         -    要先装饰get方法，再用装饰后的get加上setter去装饰set方法
    
         -    这样方法名才能和引用时候一致
    

 

## 继承

-   子类subclass；基类baseclass 也成父类、超类superclass

-   子类不能继承和调用父类的私有方法

-   执行一个方法但是类中不存在则会逐级向上寻找

-   如果有多个父类；则会依次自左向右继承属性和方法；多继承

    -   广度优先的搜索

-   子类中如果定义了`__init__`则会屏蔽父类中的`__init__`；所以需要在子类中设置`super().__init__()`

-   子类中可以定义与父类同名的方法来重写(override)父类中的类

    *   ```python
        class Animal():
            def __init__(self,name):
                print("父类中的init被调用啦！")
                self.name=name
        
        class Fly(Animal):
            pass
        
        class Bird(Fly):
            Btype=None
            def __init__(self,name):
                super().__init__(name)
                print("自己的__init__")
                print(self.name)
        print("="*20)
        dafei=Bird('大飞老师')
        print("="*20)
        ```



 

## 多态

*   ```python
    ...
    
    def feedPet(person,temp)
    	if isinstance(temp,Pet) #用isinstance()来判断对象是否为指定类；或是继承了指定类 
        	执行
        else:
            执行
    ```

*   Python中依赖isinstance()来实现多态的特点



 

## 模块

*   有功能相近的函数或类封装到一个.py文件中，就是一个模块(module)

*   模块格式

    *   ```python
        #格式1
        import operator
        #每次都需要通过 name.对象 来使用
        print(operator.add(2,3))
        #即和使用普通的函数和方法格式一致；唯一不同就要先带入，且在使用时需要写上文件前缀
        
        #格式2
        from operator import add,abs
        print(add(2,3))
        #这种格式可以不需要在使用时写上文件前缀
        
        
        from operator import *
        #默认导入模块中所有的内容
        #可以在模块中使用
        __all__=['add','abs'...] 
        #来指定*所代表的对象
        
        
        ```

*   如果模块中一些代码不希望被其他文件执行，则可以在这些语句前写上`if __name__=='__main__'`
    *   在模块中的`__name__`即为`'__main__'`,而其他文件引入后它的值为模块名

 

## 包

*   包用于存放多个模块

*   每个包都有一个`__init__.py文件`；且在导入包时会自动执行其中的内容；

*   也可以导入包时导入批量的模块

    *   ```python
        from pack import *
        r=math.divide(x,y)
        
        #在__init__文件中
        __all__ = ['math']
        #不同于从模块中导入内容的*（默认为模块中的所有内容）;在从包导入模块时，如果不指定*所对应的模块列表，则默认为空
        ```
        


*   导入包

    *   ```python
        from Math import operator
        print(operator.add(2,3))
        
        from Math.operator import add,abs
        print(add(2,3))
        ```

*   如果文件和被调用的模块在同一个包中，则可以简写

    *   ```python
        #文件名 test
        from .operator import add,abs
        print(add(2,3))
        |-Math
        |--test.yp
        |--operator.yp
        ```

*   ```python
    |-Math
    |--operator.yp
    
    |-run
    |--test.yp
    
    #在test.py中引用operator模块
    from Math.operator import *
    ```

    *   包的导入都是基于项目的

*   循环导入
    *   在项目中两个模块互相导入就会出现循环导入
    *   避免方法
        *   重构架构
        *   将导入语句放到函数内
        *   整个模块导入；调用时写上调用前缀



 

## time模块

-   import time

-   time.time()
    -   返回当前时间戳

-   time.sleep(n)
    -   延迟n秒

-   time.ctime(n)

    -   将一个时间戳转为一个本地字符串格式的时间

-   time.localtime(n)

    -   返回详细的时间戳信息;以元组格式返回

-   ```python
    second=t.time()
    print(t.ctime(second))
    #Fri Oct 28 20:52:07 2022
    print(t.localtime(second))
    #time.struct_time(tm_year=2022, tm_mon=10, tm_mday=28, tm_hour=20, tm_min=53, tm_sec=31, tm_wday=4, tm_yday=301, tm_isdst=0)
    print(t.localtime(second).tm_hour)
    #20
    ```

 

## datetime模块

*   `datetime.now()`
    *   获取当前日期和时间

*   `datetime.date(year,month,day)`类
    *   datetime.date(now)

*   ```python
    print(datetime.now())
    #2022-10-28 22:48:46.474564
    taday=datetime.date(datetime.now())
    print(taday.year,taday.month,taday.day)
    #2022 10 28
    ```

*   datetime.timedelta()

*   **未完成...**

 

## random模块

*   `random.randint(a,b)`
    *   [a,b]
*   `random.randrange(a,b)`
    *   [a,b)
*   `random,choice(可迭代对象)`
    *   返回对象中的一个随机元素
*   `random.shuffle(列表)`
    *   随机打乱列表中的元素排列
*   `random.uniform(x,y)`
    *   随机返回一个[x,y]之间的实数




## hashlib模块

-   补充：ascii码和字符的转换

    -   char(n)

    -   ord(c)

        -   c为1~127的ascii码
        -   超过范围返回Unicode码

    -   ```python
        c='我'
        n=ord(c)
        print(n)
        #25105
        print(f'{chr(n)}真帅')
        #我真帅
        ```

*   ```python
    import hashlib
    
    pwdList=[]
    password="7777777"
    pwdList.append(hashlib.md5(password.encode()).hexdigest())
    # print(pwdList)
    
    pwd=input("请输入密码:")
    pwd=hashlib.md5(pwd.encode()).hexdigest()
    
    if pwd in pwdList:
        print("登录成功！")
    else:
        print("密码错误！")
    ```






















































## 单词

