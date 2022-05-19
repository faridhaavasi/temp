from email import contentmanager

def dot_sum(file_name:str):
    file=open(file_name)
    f=file.readlines()
    content=0
    for line in f:
        for char in line:
            if char=='.':
                content+=1
    return content


print(dot_sum('persion.txt'))
    