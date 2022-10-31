# ##################################################################################
# # #输入一个原路径
# # #输入一个目标路径
# # #将文件夹下的全部内容复制到目标文件夹下
# import os



# while 1:
#     sourceDir=input("请输入源文件夹:")
#     if os.path.isdir(sourceDir):
#         break
#     else:
#         print("请输入有效文件夹路径")
# while 1:
#     aimDir=input("请输入目标文件夹:")
#     if os.path.exists(aimDir):
#         break
#     else:
#         os.mkdir(aimDir)
#         break



# fileList=os.listdir(sourceDir)

# for i in fileList:
#     with open(os.path.join(sourceDir,i),'rb') as rstream:
#         temp=rstream.read()
#     with open(os.path.join(aimDir,i),'wb') as wstream:
#         wstream.write(temp)
# print("复制完成！")
# #E:\Chromcrx

##################################################################################

#删除指定目录
# import os
# p="F:\\desinatedDir\\"

# fList=os.listdir(p)

# for i in fList:
#     newPath=os.path.join(p,i)
#     os.remove(newPath)

# os.rmdir(p)




