n = int(input())

names= []
for i in range(n):
    names.append(input())
    
for i in range(n):
    flag=False
    for j in range(i):
        if i!=j and names[i]==names[j]:
            flag=True
            break
        else:
            pass
    if flag==True:
        print('YES')
    else:
        print('NO')
            
            
