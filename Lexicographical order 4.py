str = input()
li=[]
for i in range(len(str)):
    if str[i].islower():
        li.append(str[i])

li.sort(reverse=True)

str_li=list(str)
for i in range(len(str_li)):
    if str_li[i].islower():
        char= li.pop()
        str_li[i]=char

    
str=''.join(str_li)  
print(str)
        
        
        
