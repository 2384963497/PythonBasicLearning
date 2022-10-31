
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
