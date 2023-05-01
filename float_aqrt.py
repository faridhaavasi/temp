import math
from decimal import *

n = int(input('enter n:'))
list_of_num = []
for i in range(1,n+1):
    s = float(input('enter number'))
    sq = f"The square root of {s} is {math.sqrt(s):.4f}"
    print(sq)
  
   


