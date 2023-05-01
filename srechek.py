list_od_s_un = ['O', 'I', 'A', 'U', 'E']
list_od_s_un_lower =[]
for i in list_od_s_un:
    list_od_s_un_lower.append(i.lower()) 

N = 'This is a test' 
new_n = ''
for i in N:
    if i in list_od_s_un or i in list_od_s_un_lower:
        pass
    else:
        new_n +=i

print(new_n)        