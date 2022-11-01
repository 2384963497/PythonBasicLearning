# Python02




##字符串 

* id(n)

  * 返回一个字符串的地址

* is运算

  * 判断两个对象地址是否相同

  * ==是判断两个对象值是否相同

    ```python
    a=input('a=')
    b=input('b=')##都输入同一个字符
    print(a is b)#False
    print(a == b)#True
    ```

* in和not in运算

  - s1 in s2 判断s1是否是s2的子串

###字符串切片操作 

- str[n]
  - 下标为n的字符

- str[-1]
  - 字符串第一个字符下标为0
  - 下标可取负数
  - 最后一个字符的下标为-1

- str[n:m]
  - 下标为[n,m)的字符串

- str[n: m :s]
  - 下标为[n,m)的字符串，步长为s
  - s可以取负

- str[n:]
  - 第二个参数缺省默认为结束-1

- str[:m]
  - 第一个参数缺省默认为0

- str[::]
  - 整个字符串

- str[-1:0:-1]
  - 逆序输出字符串，但是无法输出第一个字符
  - 逆序输出整个字符串str[::-1]


### 字符串的内建函数

* .captialize()
  * 将第一个字母转为大写
* .upper()
  * 将字符串转为大写
* .lower()
  * 转小写
* .title()
  * 将每个单词的首字母转为大写
* len()
  * 返回字符串长度
* .find()
  * .find(str,beg,end)可以指定查找的开始和结束
  * 未找到则返回-1
  * .rfind()、.lfind()指定不同方向的查找
* .idnex()
  * 和.find()功能一致；不过.index()没找到则报错；所以一般不用
* .replace()
  * .replace(old,new,count)
  * count是替换的次数;2则为前两个new替换为old
* .encode()
  * 将字符串转为编码后的格式；
  * 可以指定编码格式；默认为utf-8
* .decode()
  * 解码；默认也为utf-8
* .startwith()
  * 检测是否以str开头
* .endwith()
  * 检测是否以str结束
* .isalpha()
  * 检测内容是否为纯英文字母
* .isdigit()
  * 检测内容是否为纯数字
* .join()
  * 用前面的字符串连接后面参数中的内容，返回字符串
* .sprit()
  * .lsprit()、.rsprit()
  * 删除前置或者后置空格
* .split()
  * .split(str,count)
  * 以str分割字符串count次;返回分割后的**列表**
* .count()
  * .count(str)
  * 返回字符串中str出现的次数





 

## 随机数

```python
import random
 xnum = random.randint(0,9)#0到9的随机数
```

1. 使用import random
2. 使用random.randint(begin,end)

 

## 列表 

* 列表-增删改查

  * 增

    * .append(value)

      *   追加

    

    * .extend(对象)
  
      * 将对象迭代后追加到列表
  
    
  
    * .insert(对象,下标)
        * 插入之后对象从原下标处开始

  * 删
  
    * del 列表[切片]
  
        
  
    * .remove(e)
  
        * 移除列表中出现的第一个e并返回None
        * 没有e则报错
  
    
  
    * .pop([下标])
        * 删除并返回列表最后一个元素
        * 若有下标则为下标元素
  
    
  
    *   .clear() 
        *   清空列表
  
  * 改
  
      * 下标、切片、遍历+赋值操作
  
  * 查
  
      * 下标、切片、遍历

*   列表可以进行+  *运算
*   .reveres()
    *   将列表逆序排列
*   排序
    *   sorted(列表[,reveres=True])
        *   函数**不改变**列表的物理顺序
    *   列表.sort([reveres=True])
        *   方法**改变**列表的物理顺序

 

## 元组

-   定义一个只有一个元素2的元组t

    -   ```python
        t=(2,)
        ```



*   元组可以简单理解为一个不能修改的列表



 

## 字典 

*   格式

    *   ```python
        name={'key':value,'key':value...}
        ```

    *   在dict()转换的时候，对象也必须为两两成对



*   字典-增删改查

    *   增、改

        *   name['key']=value
            *   如果key已经在字典中存在则为更新
            *   不存在则为插入
        *   .update(字典)
            *   若两个字典无相同key则为两个字典的合并
            *   若有相同的key，则相同key值更新再合并

    *   删

        *   del name['key']
        *   name.pop('key'[,default])
            *   删除最后一个键值对，并返回其中值
            *   若有key则删除并返回对应键值对
            *   若没用key则报错
                *   若指定了default则不会报错，返回默认值
        *   .popitem()
            *   删除并返回最后一个键值对

        *   .clear()

    *   查
        *   字典用key代替下标
        *   name['key']
            *   若不存在key则报错
        *   .get('key'[,default])
            *   返回key对应的值
            *   没key则默认返回None，有默认值则返回默认值

*   字典方法

    *   .items()

        *   将字典转为**列表**，列表元素是由键值对两两组成的**元组**
        *   在遍历字典时，可以用.items()加两个变量配合遍历

    *   .keys()

        *   将字典转为列表，列表元素是key

    *   .values()

        *   将字典转为列表，列表元素是value

    *   ```python
        x={'name':'小虎','score':2200,'age':24,'pos':'mid','age':26}
        
        r=x.items()
        print(r)
        r=x.keys()
        print(r)
        r=x.values()
        print(r)
        '''
        dict_items([('name', '小虎'), ('score', 2200), ('age', 26), ('pos', 'mid')])
        dict_keys(['name', 'score', 'age', 'pos'])
        dict_values(['小虎', 2200, 26, 'mid'])
        '''
        ```

*   dict.fromkeys(seq[,value])

    *   将seq转为字典，seq迭代对象为key值为None若指定了value则为value

        *   ```python
            l=[0,1,2,3,4,5]
            r=dict.fromkeys(l,'temp')
            #{0: 'temp', 1: 'temp', 2: 'temp', 3: 'temp', 4: 'temp', 5: 'temp'}
            ```

 

## 集合

-   集合(set)
    -   {6,48,'f',8,(15,3)}
-   创建一个空集合
    -   s=set()
-   增
    -   s.add()
    -   s.update()
        -   将参数迭代一次后对象加入到集合
-   删
    -   s.remove(e)
    -   s.pop()
    -   s.clear()
    -   s.discord()
        -   同.remove()，单.discord()没有元素也不报错
-   {1,2,3}=={3,1,2}====>True
-   集合运算
    -   交
        -   s1&s2
    -   并
        -   s1|s2
    -   差
        -   s1-s2
    -   对称差集
        -   s1
-   forzenset(s)
    -   返回一个不可变集合s

 

## 海龟绘图

*   转向
    *   turtle.left(n)
        *   n是角度
    *   turtle.right(n)
*   改变速度
    *   turtle.speed(n)
    *   n取值0-1 1最慢0最快
*   前进
    *   turtle.forward(n).
*   抬起和放下画笔
    *   turtle.penup()
    *   turtle.pendown()
*   画笔大小
    *   turtle.pensize(n)
    *   n像素
*   填充颜色
    *   指定填充颜色 turtle.fillcolor()
        *   turtle.colormode(0|255)
        *   颜色关键字
        *   或者十六进制表示  turtle.fillcolor(”#f0f“)
    *   开始填充turtle.begin_fill()
    *   绘制封闭图像
    *   结束填充turtle.end_fill()
*   画圆
    *   turtle.circle(n)
    *   n为半径
*   隐藏海龟
    *   turtle.hideturtle()
*   文字
    *   write(文本,font=("字体","字号","italic","bold"))




## 函数 

*   定义和调用格式

    ```python
    #定义
    def functionname( parameters ):
       "函数_文档字符串"
       function_suite
       return [expression]
    
    #调用
    printme("我要调用用户自定义函数!")
    ```

-   可变参数和不可变参数

    -   不可变参数
        -   int，float，string，tuple
    -   其他的参数都为可变参数

-   参数

    -   必备参数

        -   调用函数时要求参数个数和顺序必须一一对应

    -   关键字参数

        -   ```python
            #定义
            def printinfo( name, age ):
            #调用
            printinfo(age=12,name='xiaoming')
            ```

        -   使用为关键字赋值的方法，可以让参数之间的顺序不重要

        -   如果一个参数使用看关键字参数传入，则之后的参数必须用关键字的方式传入

        -   ```python
            def printInfo(**args):
                print(args)
            
            printInfo(name='xiaohu',mid=2200,math=66.6)
            
            stu01={'name':'销户','Chinese':99,'math':71,'English':100,'mid':22.00}
            printInfo(**stu01)
            '''
            输出
            {'name': 'xiaohu', 'mid': 2200, 'math': 66.6}
            {'name': '销户', 'Chinese': 99, 'math': 71, 'English': 100, 'mid': 22.0}
            '''
            ```

            -   l4:若参数为可变参数**开头而且在传入参数时使用的是关键字参数；则会将传入的关键字和值组成键值对；最后再转为dict类型的对象
            -   l7:如果传送的原对象已经是dict，则需要使用**name的格式将原dict拆包再将实参传给\*\*args
            -   *对象 可以拆列表和元组
            -   总结:**如果是dict对象:则会将对象拆包；\*\*是函数的参数:则代表将传入的关键字参数key=val打包成键值对，最后在全部转一个dict类型对象

    -   默认参数

        -   ```python
            def printinfo( name,age,country="China" ):
            ```

        -   设置参数没有传入时的默认值

    -   不定长参数 

        -   ```python
            def fun1(name,*score)
            ```

        -   如果传入的参数超过两个则将其他参数**打包成元组**存放在不定长参数中

            -   ```python
                def fun1(name,*score)
                
                fun1('1',[12,635,1])
                #score >> ([12,635,1])
                fun1('1',[12,635,1],5,9)
                #score >> ([12,635,1],5,9)
                ```

        -   不定长和必备参数使用时要避免二义性

-   变量的作用域

    -   定义在一个函数内的变量为局部变量 其他为全局变量

    -   使用global 可以在函数中定义全局变量

    -   函数中修改  **不可变类型的变量**，只在函数范围内起作用；不影响原变量的值

        -   ```python
            global a
            a=6
            
            def fun():
                a='a'
                print(a)
            
            print(a)
            fun()
            print(a)
            '''
            6
            a
            6
            '''
            ```

    -   l5:只有在函数中声明一次 变量为全局变量才能修改到原变量

        -   ```python
            global a
            a=6
            
            def fun():
            	global a
                a='a'
                print(a)
            
            print(a)
            fun()
            print(a)
            '''
            6
            a
            a
            '''
            ```

    -   函数中修改 **可变类型的变量**，可以修改到原变量的值,而无需声明global

        -   ```python
            a={'name':'xiaohu',"team":'rng','pos':'mid'}
            
            def fun():
                a['pos']='top'
                print(a)
                
            print(a)
            fun()
            print(a)
            '''
            {'name': 'xiaohu', 'team': 'rng', 'pos': 'mid'}
            {'name': 'xiaohu', 'team': 'rng', 'pos': 'top'}
            {'name': 'xiaohu', 'team': 'rng', 'pos': 'top'}
            '''
            ```

    -   locals():查看当前函数中的内部变量和内部函数地址

    -   globals():查看全局变量和函数地址

-   匿名函数

    -   一般格式 fun=lambda 参数1,参数2:表达式

    -   匿名函数可以作为函数参数



*   内部函数
    *   python支持函数内部嵌套函数
    *   内部函数可以访问外部函数的变量
    *   如果需要改外部函数的不可变类型，则要加nonlocal 变量名
    *   内部函数修改全局不可变变量则需要加global 变量名  

 

## 单词

* ignore    忽略 

* attribute 属性

* extend  延升，扩大

* traceback 回溯

* argument 参数；争吵

* syntax  语法

- iteration  迭代
- enumerate 枚举

* element  元素
* callable  可调用的
* keymap  快捷键
* current  当前的
* assignment  赋值，任务，工作
* immutable  不可变的
