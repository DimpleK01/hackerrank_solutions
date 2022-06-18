n= int(input())
if n!=0:
    str = input()

def is_palindrome(n, str):
    count=0
    for i in str:
        flag = True
        if str.count(i)==n:
            pass
        
        elif str.count(i)%2==0:
            pass
        
        else:
            count+=1
            if count>1:
                flag =False
                break
        
    if flag==True:
        print('YES')
    else:
        print('NO')
        
if n==0:
    print("YES")
    
else:
    is_palindrome(n,str)
        
                
