def remix(s:str,ary:list):
    new_s=""
    for i in ary:
        #print(s[i])
        new_s+=s[i]
    return new_s

print(remix("PlOt", [1, 3, 0, 2])) #➞ "ltPO"

print(remix("computer", [0, 2, 1, 5, 3, 6, 7, 4])) #➞ "cmotperu"

#link of task :
# https://backendbaz.ir/practice/4392/
