li= list(input().split())

str=li[0]
k=int(li[1])

if k!=0:
    for i in range(1,len(str)+1):
        if i%k==0:
            i-=1
            str=str.replace(str[i], str[i].capitalize(),1)
        
print(str)
