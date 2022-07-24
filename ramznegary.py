ALPHA_BET=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ALPHA_BET_CERIPTO=ALPHA_BET[::-1]
s='apple'
new_s=[]
s=s.upper()
for i,n in enumerate(ALPHA_BET):
    for j in s:
        if j==n:
            new_s.append(ALPHA_BET_CERIPTO[i])

             

print(''.join(new_s).lower())

