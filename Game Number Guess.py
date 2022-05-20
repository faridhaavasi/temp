from random import randint
name=input('enter name')
ran_computer=randint(1,99)
def easy():
    for i  in range(1,11):
        hads=int(input('enter yot nume'))
        if hads>ran_computer:
            print('bozorgtareh hadset')
        elif  hads<ran_computer:
            print('kochicktareh hadset') 
        else:
            print('vou ven %s wow!!!!!!'%name)
    else:
        print('you lose%s'%name)


def hard():
    for i  in range(1,8):
        hads=int(input('enter yot nume'))
        if hads>ran_computer:
            print('bozorgtareh hadset')
        elif  hads<ran_computer:
            print('kochicktareh hadset') 
        else:
            print('vou ven %s wow!!!!!!'%name)
    else:
        print('you lose%s'%name)
level=input('enter lovel easy or hard')
if level=="easy":
    easy()
elif level=="hard":
    hard()
else:
    print('level is a have in easy or hard')        
