s="ApPle"
new_s=s[::-1]
l_s=[]
#print(new_s)
for i in new_s:
    if i.lower():
        l_s.append(i.upper())
    else:    
        l_s.append(i)

for i,v in enumerate(l_s):
    if v =='A':
        l_s[i] ='B'
    if v=='B':
        l_s[i]='C'    
    if v =='C':
        l_s[i] ='D'    
    if v=='E':
        l_s[i] = 'F'
    if v=='F':
        l_s[i] = 'G'
    if v=='G':
        l_s[i] = 'H'
    if v=='H':
        l_s[i] = 'I'
    if v=='I':
        l_s[i] = 'J'
    if v=='J':
        l_s[i] = 'K'
    if v=='K':
        l_s[i] = 'L'
    if v=='L':
        l_s[i] = 'M'
    if v=='M':
        l_s[i] = 'N'
    if v=='N':
        l_s[i] = 'O'
    if v=='O':
        l_s[i] = 'P'
    if v=='P':
        l_s[i] = 'Q'
    if v=='Q':
        l_s[i] = 'R'
    if v=='R':
        l_s[i] = 'S'
    if v=='S':
        l_s[i] = 'T'
    if v=='T':
        l_s[i] = 'U'
    if v=='U':
        l_s[i] = 'V'
    if v=='V':
        l_s[i] = 'W'
    if v=='W':
        l_s[i] = 'X'
    if v=='X':
        l_s[i] = 'Y'
    if v=='Y':
        l_s[i] = 'Z'
    if v=='Z':
        l_s[i] = 'A' 








total_s=''.join(l_s)
print(total_s)      



  
