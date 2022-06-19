n = int(input())
li=list(map(int, input().split()))
sum=[]
for i in range(len(li)):
    add=li[i]
    sum.append(add)
    for j in range(i,len(li)):
        if i!=j:
            add+=li[j]
            sum.append(add)
if 0 in sum:
    print('Yes')
else:
    print('No')
