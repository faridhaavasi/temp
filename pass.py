s='im farid im very happy im hangry very very sooon'
st=''
l_word=s.split()
for i in l_word:
    #print('kalamat:',i)
    aval=(i[0])
    #print('aavalkalamat',aval)
    st+=aval
#print(st)    
aval_pass=st
#print(aval_pass)
n_pass=''
for i in aval_pass:
    if i=='a':
        n_pass=+'@'
    elif i=='i':
        n_pass+='1'
    elif i=='o':
        n_pass+='0'
    elif i=='s':
        n_pass+='*'
    elif i=='c':
        n_pass+=')'
    elif i=='v':
        n_pass+='&'

print(n_pass)
list_pass=[]
for i in n_pass:
    list_pass.append(i)

#print(list_pass)
list_new_pass=[]
print(list_pass[::2])
list_new_pass=list_pass[::2]
final_var=[]
for i in list_new_pass:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5"or i=="6" or i=="7" or i=="8" or i=="9":
        var=(int(i))
        final_var.append(var) 

print(final_var)