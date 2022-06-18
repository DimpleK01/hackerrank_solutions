n = int(input())
inp= []
for i in range(n):
    inp.append(int(input()))
for i in inp:
    k=i
    for j in range(1,i+1):
        print((j*'*')+((k*2)-2)*'#'+(j*'*'))
        k-=1
    print()
   
