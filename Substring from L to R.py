n = int(input())
str =  input()
li = list(map(int, input().split()))

start= li[0]
end = li[1]+1
print(str[start: end])
