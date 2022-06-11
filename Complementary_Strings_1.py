s1=input()
s2=input()

alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s3=s1+s2
flag=True
for i in alph:
    for j in s3:
        if (i not in s3) or (s3.count(i)>1) :
            flag=False
            break
    if flag==False:
        print('no')
        break
if flag==True:
    print("yes")

            
    

