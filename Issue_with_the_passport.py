n = int(input())
passport = list(map(str, input().split()))

no_dup =[]
for i in passport:
    if i not in no_dup :
        no_dup.append(i)
            
for i in no_dup:
    print(i, end=" ")
