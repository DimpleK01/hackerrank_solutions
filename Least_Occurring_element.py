
    

n= int(input())
arr= list(map(int, input().split()))

duplicates = dict((x,arr.count(x)) for x in set(arr))

duplicates = dict(sorted(duplicates.items(), key=lambda item: item[1]))
values=list(duplicates.values())
n = values.count(values[0]);
li=[]
keys=list(duplicates.keys())
for i in range(n):
    li.append(keys[i])
li.sort(reverse=True) 
for i in range(len(li)):
    print (li[i], end=" ")

    
    
