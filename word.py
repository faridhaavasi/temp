def alternatingCaps(s:str):

    list_of_s=list(s)
    list_of_s_teotal=[]
    for i in list_of_s:
        if i==' ':
            pass
        else:
            list_of_s_teotal.append(i)
    list_of_s_teotal_finall=list_of_s_teotal[::2]
    #print(list_of_s_teotal_finall)
    list_of_s_teotal_finall_up=[]
    for i in list_of_s_teotal_finall:
        list_of_s_teotal_finall_up.append(i.upper())
        #print(i.upper())
    for i,v in enumerate(list_of_s):
        if v.upper() in list_of_s_teotal_finall_up:
            #print(i,v)
            list_of_s[i]=v.upper()
    print(''.join(list_of_s))

alternatingCaps("Hello") #➞ "HeLlO"

alternatingCaps("How are you?") #➞ "HoW aRe YoU?"

alternatingCaps("OMG this website is awesome!") #➞ "OmG tHiS wEbSiTe Is AwEsOmE!"
# link of task:https://backendbaz.ir/practice/4468/
