def alternatingCaps(s:str):
    l=list(s)
    #print(l)
    new_l=[]
    for i ,v in enumerate(l):
        if v == ' ':
            pass
        else:
            new_l.append(v)
    list_of_up=[]
    list_of_w=new_l[1::2]        
    for i in list_of_w:
        #print(i.upper())
        list_of_up.append(i.upper())

    #print(list_of_up)
    for i ,v in enumerate(l):
        if v.upper() in list_of_up:
            #print(i,v.upper())
            l[i]=v.upper()
    
    print(''.join(l))    

alternatingCaps("Hello") #➞ "HeLlO"

alternatingCaps("How are you?") #➞ "HoW aRe YoU?"

alternatingCaps("OMG this website is awesome!") #➞ "OmG tHiS wEbSiTe Is AwEsOmE!"
# link of task:https://backendbaz.ir/practice/4468/