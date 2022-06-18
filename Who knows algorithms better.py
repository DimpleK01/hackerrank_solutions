
li= list(map(int,input().split()))
n=li[0]
c=li[1]
m=[]
for i in range(2):   
    single_row = list(map(int, input().split()))   
    m.append(single_row)  

Lp=0
Rp=0
x=0
for i in range(n):
    x+=m[1][i]
    Lp+=max(0,(m[0][i]-c*x))
    
x=0
for i in range(n-1,0,-1):
    x+=m[1][i]
    Rp+=max(0,(m[0][i]-c*x))
    
if Lp>Rp:
    print("Limak")
elif Rp>Lp:
    print("Radewoosh")
elif Rp==Lp:
    print("Tie")
    
