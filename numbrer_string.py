def countAll(n:str):
    list_number=['0','1','2','3','4','5','6','7','8','9']
    number=0
    s=0

    for i in n:
        if i==" ":
            pass
        elif i in list_number:
            number+=1
        else:
            s+=1
    print(number,'numbers',s,'string')            

countAll("Hello World") #➞ array("حروف" =>  10, "اعداد" => 0)

countAll("H3ll0 Wor1d") #➞ array("حروف" =>  7, "اعداد" => 3)

countAll("149990") #➞ array("حروف" => 0, "اعداد" => 6)

# link of task: https://backendbaz.ir/practice/4385/