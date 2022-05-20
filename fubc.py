def zarayeb(num, length):
    li=[]
    for i in range(1,length+1):
        re=num*i
        #print(re)
        li.append(re)
    return li

print(zarayeb(7,5))        
print(zarayeb(12,10))