def maximum(li, str):
    n=li[0]
    k=li[1]
    rem=[int(str)%k]
    if len(str)>1:
        for i in range(n):
            temp = int(str[:i]+str[i+1:])
            rem.append(temp%k)
    
    print(max(rem))

t=int(input())
for i in range(t):
    li = list(map(int, input().split()))
    str= input()
    maximum(li,str)
