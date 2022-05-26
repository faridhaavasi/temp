def letterCheck(l:list):
    #print(len(l))
    if len(l)==2:
        conter=0
        s1=''.join(l[0])
        #print(s1)
        s2=''.join(l[1])
        for i in s2:
            if i in s1 or i.upper() in s1.upper():
                conter+=1
            else:
                pass
        #print(conter)    
        if len(s2)==conter:
            return True
        else:
            return False        
    else:
        pass

print(letterCheck(["trances", "nectar"])) #➞ true

print(letterCheck(["compadres", "DRAPES"]))# ➞ true

print(letterCheck(["parses", "parsecs"]))# ➞ false