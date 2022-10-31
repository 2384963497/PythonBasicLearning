

class1=[{'name':'小虎','score':2200},{'name':'厂长','score':4396},{'name':'大飞','score':32},{'name':'Tian','score':4397}]

# for n in range(len(class1)):
#     for i,keyname in enumerate(class1[n]):
#         keyval=class1[n][keyname]
#         # print(keyname,keyval)
#         if keyname=='score' and keyval>2200:
#             print('{}>一虎'.format(class1[n]['name']))

for n in range(len(class1)):
    for keyname,keyval in class1[n].items():
        # print("keyname:{}={}    ".format(keyname,keyval),end='')
        if keyname=='score' and keyval<=2200:
            class1[n][keyname]+=10000
    print("")
print(class1)