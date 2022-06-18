n = int(input())

number = str(input())
answer=[]
count=0
stairs=number.count('1')
for i in range(len(number)):
    if number[i]=='1':
        if i!=0 :
            answer.append(count)
        if i==len(number)-1:
            answer.append(1)
        count=1
    elif number[i]!=' ':
        count+=1
        if i==len(number)-1:
            answer.append(count)

print(stairs)

for i in answer:
    print(i, end=' ')

    
    
    
