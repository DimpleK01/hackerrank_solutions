n1,n2=[int(x) for x in input().split()]


arr1 = list(map(int,input().strip().split()))[:n1]
arr2 = list(map(int,input().strip().split()))[:n2]

arr1.sort()
arr2.sort(reverse=True)

arr3=arr1+arr2

for i in range(len(arr3)):
    print(arr3[i], end=" ")
