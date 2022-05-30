def longestWord(s:str):
    s_total=s.split()
    max_lenght=0
    max_s=''
    list_of_s_total=[]
    for i in s_total:
        list_of_s_total.append(i)
    for i,v in enumerate(list_of_s_total):
        lenght=len(v)
        #print(i,v,lenght)
        if lenght > max_lenght:
            max_lenght=lenght
            max_s=v

    #print(max_lenght)
    print(max_s)

longestWord("Hello darkness my old friend") #➞ "darkness"

longestWord("Hello there mate") #➞ "Hello"

longestWord("Kayla's toy is plastic") #➞ "Kayla's"

#link of task : https://backendbaz.ir/practice/4384/
