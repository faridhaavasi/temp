s='fadssriddo'
d=[]
di={}
index=[]
for i in s:
    d.append(i)
for i , v in enumerate(s):
    if v in d:
        print(v,i)
        index.append(i)

