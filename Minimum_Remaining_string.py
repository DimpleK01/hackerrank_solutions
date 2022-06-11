s1= input()
index=0
rev=s1[::-1]
for i in range(len(s1)):
    if(s1[i]==rev[i]):
        index+=1
    else:
        break
s1=s1[index:len(s1)-index]
if(s1==""):
    print("Minimal string is empty")
else:
    print(s1)
