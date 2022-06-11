n = int(input())
d=[]
for i in range(n):
    d.append(input())
q=int(input())
qts=[]
for i in range(q):
    qts.append(input())

for i in qts:
    flag=False
    for j in range(len(i)):
        prefix=i[:j]
        suffix=i[j:]
        if prefix in d and suffix in d:
            flag=True
            break
    if flag==True:
        print("Yes")
    else:
        print("No")
