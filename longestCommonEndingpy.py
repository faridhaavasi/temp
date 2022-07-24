s1="multiplication"
s2="ration"
list_of_w=[]
for i , v in enumerate(s1[::-1]):
     for i in s2[::-1]:
         if v == i:
            print(v)
            list_of_w.append(v)
print(''.join(list_of_w))
