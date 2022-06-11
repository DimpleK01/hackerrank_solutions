
n=int(input())
arr=list(map(int, input().split()))
li=[]

for i in range(len(arr)):
    sum=arr[i]
    index=0
    for j in range(i,len(arr)):
        index+=1
        if(i!=j):
            sum+=arr[j]
            if(sum==0):
                li.append(index)
                
                
print(max(li))
