def fun():
    return {'name':'tool','function':'strip'}
    # return ('name','strip'),2

# r,m=fun()
# print(r,'\n',m)
r=fun()

for k,v in enumerate(r):
    print("{}:{}".format(k,v))