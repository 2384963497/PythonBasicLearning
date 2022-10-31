# 利用字典 实现用户注册功能


user={}
users=list()

print('-'*15+"欢迎来到注册系统"+'-'*15)
print('-'*46)

userName=input("请输入用户名：")
user['userName']=userName

while True:
    userPass=input("请输入密码")
    while userPass.isdigit() or userPass.isalpha():
        userPass=input("密码必须为数字和字符的组合!请重新输入!:")

    userCheck=input("请再一次输密码:")
    if userPass==userCheck:
        user["userPass"]=userPass
        break
    else:
        print("-"*46+'\n'+'两次密码不一致请重新设置密码\n')

userEmail=input("请输入用户邮箱:")
user["userEmail"]=userEmail

users.append(user)
print(users)