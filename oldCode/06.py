# class1=[{'name':'小虎','score':2200},{'name':'厂长','score':4396},{'name':'大飞','score':32},{'name':'Tian','score':4397}]
# print(class1[0].values())
# x={'name':'小虎','score':2200,'age':24,'pos':'mid','age':26}

# r=x.items()
# print(r)
# r=x.keys()
# print(r)
# r=x.values()
# print(r)
# print(x)

# x.update({'hero':'图奇'})

# print(x)

# l=[0,1,2,3,4,5]
# r=dict.fromkeys(l,'temp')
# print(r)
# sorted(l,reverse=True)
# l.sort(reverse=True)
# l.reverse()
# print(l)
# print(l)
# print(l)
# l=['qew','name','ds','go.']
# print("+".join(l))
# global a
# a=6

# def fun():
#     global a
#     a='a'
#     print(a)

# print(a)
# fun()
# print(a)
# print(isinstance(23,int))
# with open("tt.txt",'rb') as rstream:
#     temp=rstream.readline()
# with open("tt.txt",'rb') as rstream:
#     temp1=rstream.readlines()
#     # temp1=rstream.readlines()

# print("="*30)
# print(temp)
# print("="*30)
# print(temp1)

#返回当前文件夹的绝对路径
# import os
# t=os.getcwd()
# print(t)
# print(os.path.abspath(os.path.dirname(__file__)))

# a=6
# b=6
# print(f"{a}的{b}次方为{a**b}")

#输出有元组组成的列表，元组元素的第一个元素是偶数，第二个元素的奇数 0<=x,y<=5
#[(偶数,奇数),(偶数,奇数),(偶数,奇数)....]
# num=[(x,y) for x in range(6) for y in range(6) if (x%2==0 and y%2==1)]
# print(f"所得到的列表为:{num=}")

#利用字典推导式 交换字典中的key和value

# x={'name':'小虎','score':2200,'pos':'mid','age':2200}

# x={val:key for key,val in x.items()}
# print(f"处理后的x为{x}")


#生成器

#生成一个2的0次方 到 2的n次方的列表并输出

# n=int(input("请输入所求列表的长度:"))
# gener=(2**x for x in range(100000))
# numList=[]
# for i in range(n):
#     numList.append(next(gener))
# print(f"生成的列表为:{numList}")

#利用生成器 生成并输出指定长度的斐波拉契数列
# def func(len):
#     count=0
#     n=1
#     count+=1
#     yield 1
#     m=1
#     count+=1
#     yield 1
#     while count<len:
#         n,m=m,m+n
#         count+=1
#         yield m
# try:
#     n=int(input("请输入需要生成的斐波拉契数列的长度(1,50):"))
#     gen=func(50)
#     for i in range(n):
#         print(f"第{i+1}项是:{next(gen)}")
# except Exception:
#     print("长度不能超过50!!!\n")
    
# print("程序结束！")

# def fib(len):
#     a,b=0,1
#     n=0
#     while n<len:
#         yield b
#         a,b=b,a+b
#         n+=1
#     yield "已经超出了生成范围了！！！"

# n=int(input("请输入需要生成的斐波拉契数列的长度(1,50):"))
# gen=fib(50)
# print(f"gen的类型为:{type(gen)}")

# for i in range(n):
#     temp=next(gen)
#     if isinstance(temp,int):
#         print(f"第{i+1}项:{temp}")
#     else:
#         print(temp)
#         break
# print("="*30+'\n程序结束！')

# class Student():
#     studentCount=0
#     name="XiaoMing"
#     score=777

#     def __init__(self) -> None:
#         Student.studentCount+=1

#     def showInfo(self):
#         print(f"姓名:{self.name},分数:{self.score}")
#     @classmethod
#     def showTatal(cls):
#         print(f"一共有{cls.studentCount}名学生录入了信息")
# Student.showTatal()
# Xh=Student()
# Xh.name="小虎"
# XM=Student()
# Uzi=Student()
# Mark=Student()
# Student.showTatal()
# Xh.showInfo()
# Student.showTatal()
# Xh.showTatal()

# class Student():
#     def __init__(self):
#         name=None
#         score=None
#     def __call__(self, *args, **kwds):
#         print(f"姓名:{self.name}")

# Xh=Student()
# Xh.name="xiaohu"
# Xh()
# class man:
#     def __init__(self):
#         self.name="大飞"
#         self.text="ping太高了"
#     def __del__(self):
#         print(f"{self.name}寄咯！")

# man1=man()
# temp=man()

# print("程序开始")
# del man1
# del temp
# print("程序结束")

# class Book:
    
#     def __init__(self) -> None:
#         self.name=None
#         self.price=None
#     def __str__(self):
#         return (f"书本的名称为:{self.name}\n价格为:{self.price}")

# itake=Book()
# itake.name="Python零基础到项目实战"
# itake.price=86
# temp=itake
# print(temp.name)
# print(itake)

# class Std:
#     def __init__(self,name,score) -> None:
#         self.__name=name
#         self.__score=score
    
#     def setScore(self,newscore):
#         if isinstance(newscore,int) or isinstance(newscore,float):
#             self.__score=newscore
#         else:
#             print("类型错误！")

#     def getName(self):
#         return self.__name
#     def getScore(self):
#         return self.__score

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self,temp):
#         self.__name=temp

#     @property
#     def score(self):
#         return self.__score
        
# clearLove=Std("厂长",2200)
# print(f"名字为:{clearLove.name},分数为:{clearLove.score}")
# clearLove.name="明凯"
# print(f"名字为:{clearLove.getName()},分数为:{clearLove.getScore()}")





















