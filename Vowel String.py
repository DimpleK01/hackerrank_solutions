str = input()

vowels= ['a','e','i','o','u']
str = str.lower()

flag=True
for i in vowels:
    if str.count(i)==0:
        flag = False
        break
if flag==True:
    print('Accepted')
else:
    print('Not Accepted')
        
