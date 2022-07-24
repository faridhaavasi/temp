def noYelling(s:str):
    l_s=s
    new_ls=[]   
    #print(l_s)
    for i in l_s:
        #print(i)
        if i !="?" and i!="!":
            new_ls.append(i)
    if "?" in s:
        new_ls.append("?")
    elif "!" in s:
        new_ls.append("!")
    else:
        pass
    print(''.join(new_ls))

noYelling("What went wrong?????????") #➞ "What went wrong?"

noYelling("Oh my goodness!!!") #➞ "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!") #➞ "I just!!! can!!! not!!! believe!!! it!"
#/ فقط علامت های تکراری انتهای جمله حذف شوند.

noYelling("Oh my goodness!") #➞ "Oh my goodness!"
#// جملاتی که 0 یا 1 علامت در انتهای آنها هست، تغییری نکنند

noYelling("I just cannot believe it.") #➞ "I just cannot believe it."

# link task:https://backendbaz.ir/practice/4394/
