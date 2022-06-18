str = input()

for i in str:
    if str.count(i)>1:
        str = str.replace(i,i.capitalize())
        
print(str)
