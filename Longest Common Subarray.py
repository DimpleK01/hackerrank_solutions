inp = list(map(int, input().split()))
N= list(map(int, input().split()))
M= list(map(int, input().split()))

size=[]
count=0
for i in range(inp[0]):
    for j in range(inp[1]):
        if N[i]==M[j]:
            count=0
            k=i
            l=j
            while not(k>=inp[0] or l>=inp[1]) and N[k]==M[l]  :
                k+=1
                l+=1
                count+=1
        size.append(count)
        

print(max(size))
        
                
                
