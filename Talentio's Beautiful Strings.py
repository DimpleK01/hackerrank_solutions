import math
n = int(input())
str = input()
char = input()

def beautiful_str(n,str,char):
    n_ceil = math.ceil(n/2)
    count =0
    for i in str:
        if i == char:
            count+=1
    
    if count >= n_ceil:
        return 'YES'
    else:
        return 'NO'
    
print(beautiful_str(n,str,char))
