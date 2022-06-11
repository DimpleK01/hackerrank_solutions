s1, s2 =input().split()

length= min(len(s1),len(s2))

s1=s1[:length]
s2=s2[:length]

s3=s1+s2
print(s3)
