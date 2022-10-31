def func(temp):
    if(len(temp)==1):
        return temp[0]
    else:
        return temp[-1]+func(temp[0:-1])


s="1234567"

print(func(s))
