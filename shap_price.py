def getPrices(s:str):
    list_of_shap=["ice cream ($5.99)", "banana ($0.20)", "sandwich ($8.50)", "soup ($1.99)"]

    list_of_price=[5.99, 0.2, 8.50, 1.99]
    if s in list_of_shap:
        meno_shap={}
        for i in list_of_shap:
            for v in list_of_price:
                meno_shap[i]=v
        
        print(meno_shap[s])       
    else:
        print('s is not how a meno')            
   
getPrices("salad ($4.99)")        