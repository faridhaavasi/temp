def primeCount(a,b):
    c=0
    for n in range(a,b):
        res=True
        if n>1 :
            for i in range(2,n):
         
                if n%i==0:
                    res=False
                else:
                    pass

            if res==True:
                c+=1

        print(n,":",res)
    print(c)
primeCount(1, 10)# 4

primeCount(1, 100) # 25           

primeCount(1, 1000) # 168
#link of task:https://backendbaz.ir/practice/4383/