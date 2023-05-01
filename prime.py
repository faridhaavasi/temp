def prim(n):
    m = n/2
    m = int(m)
    for i in range(2, m+1):
        if m % i == 0:
            return False
        else:    
            return True    

cont = 0
for i in range(1,10000):
    if prim(i):
        cont += 1
print(cont)        


