n = int(input())
li=[]
for i in range(n):
    li.append(input())
    
q = int(input())
questions= [list(map(int,input().split())) for i in range(q)] 

for i in range(q):
    M= questions[i][0]
    X= questions[i][1]
    prefix=li[0][:X]
    
    
    for j in range(M):
        index=0
        for k in range(min(len(prefix),len(li[j]))):
            if prefix[k]==li[j][k]:
                index+=1
                
            else:
                break
        if(index>=X):
            flag=True
        else:
            flag=False
            
    if flag==True:
        print("Yes")
    else:
        print("No")
            
        
            
