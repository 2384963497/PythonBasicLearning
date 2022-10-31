import os
p=input("请输入文件夹路径:")
tail=input("请输入需要删除的文件后缀(例如: .jpg .mp4):")
pList=os.listdir(p)

for temp in pList:
    # print(os.path.splitext(os.path.join(p,temp)))
    if os.path.splitext(os.path.join(p,temp))[1] == tail:
        # print(os.path.splitext(os.path.join(p,temp)))
        os.remove(os.path.join(p,temp))
        print("成功！")

# print(pList)
