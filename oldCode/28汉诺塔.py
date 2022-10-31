count=0
def func(len,source,via,to):
    global count
    if len>0:
        func(len-1,source,to,via)
        print(f"move {source} to {to}")
        count+=1
        func(len-1,via,source,to)
func(10,'A','B','C')
print("==================\n一共%d个步骤"%count)