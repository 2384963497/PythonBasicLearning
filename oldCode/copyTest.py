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



