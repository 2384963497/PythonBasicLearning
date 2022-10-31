# def func(n):
#     if n==1:
#         return 1
#     return func(n-1)*n

# print(func(6))

# s=set((6,3,2,4))
# print(s)
# s.update("563")
# print(s)

# txt=open(r"D:\002MyCode\Python\aim.txt","w+",)

# print(txt.writable())
# print(txt.readable())
# txt.write('''def scoreInfo(*scores,name):
#     sum=0
#     for i in scores:
#         sum+=i
#     print("{}同学的总分为:{}\n".format(name,sum))


# stu01={'name':'销户','Chinese':99,'math':71,'English':100,'mid':22.00}
# scoreInfo(stu01['Chinese'],stu01['math'],stu01['English'],stu01['mid'],name=stu01['name'])
# ''')
# txt.close()
# txtrd=open(r"D:\002MyCode\Python\aim.txt","rt",)
# x=txtrd.read(10)
# print(x)
# txt.write([1,2,3,5,4,5,6,2,1])
# txt=open(r"D:\002MyCode\Python\aim.txt",mode="a",)
# txt.writelines(['\n100','2','3','5','4','5','6','2','1'])
# txt.close()
# txt=open(r"D:\002MyCode\Python\aim.txt","r",)
# print(txt.read())

# txt=open(r"D:\002MyCode\Python\aim.txt",'a')
# txt.write("这是追加上的第一条语句")
# txt.write("\n这是追加上的第二条语句")
# txt=open(r"D:\002MyCode\Python\aim.txt",'r')
# print(txt.read())

# txt.close()
# import os
# with open(r"D:\002MyCode\Python\p1.jpeg",'rb') as stream:
#     temp=stream.read()
#     print(os.path.dirname(__file__))
    

# with open(r"D:\002MyCode\Python\turtleAndRabbit\p3.jpeg",'wb') as stream:
#     stream.write(temp)
#     print(os.path.dirname(__file__))

# 将任意一个文件复制到当前目录
# import os
# sourcePath=r"F:\gal\Conteen\JIUGUAN3\2\readme.txt"
# with open(sourcePath,"rb") as rstream:
#     temp=rstream.read()


# fName=sourcePath[sourcePath.rfind("\\")+1:]

# with open(os.path.join(os.path.dirname(__file__),fName),'wb') as wstream:
#     wstream.write(temp)
# print(os.path.join(os.path.dirname(__file__),fName))


#输入任意文件名，将其保存到当前文件夹
# F:\网课\Web\01.任务一：PC端静态网页应用开发及项目.rar
#F:\gal\Mirror\Mirror1\steam_appid.txt
import os
sourceName=input("请输入源文件完整路径名称:")
sourceName.replace('\\','\\\\')

with open(sourceName,"rb") as rstream:
    temp=rstream.read()

with open(os.path.join(os.path.dirname(__file__),sourceName[sourceName.rfind('\\')+1:]),"wb") as wstream:
    wstream.write(temp)

print("复制成功！")


