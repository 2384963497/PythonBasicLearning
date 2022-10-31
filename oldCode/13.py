from sys import stderr


def scoreInfo(*scores,name):
    sum=0
    for i in scores:
        sum+=i
    print("{}同学的总分为:{}\n".format(name,sum))


stu01={'name':'销户','Chinese':99,'math':71,'English':100,'mid':22.00}
scoreInfo(stu01['Chinese'],stu01['math'],stu01['English'],stu01['mid'],name=stu01['name'])