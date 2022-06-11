


def printdata(arr, i, j, m, n):

    if (i >= m or j >= n):
        return

    for p in range(i, n):
        print(arr[i][p], end=" ")

    for p in range(i + 1, m):
        print(arr[p][n - 1], end=" ")

    if ((m - 1) != i):
        for p in range(n - 2, j - 1, -1):
            print(arr[m - 1][p], end=" ")


    if ((n - 1) != j):
        for p in range(m - 2, i, -1):
            print(arr[p][j], end=" ")

    printdata(arr, i + 1, j + 1, m - 1, n - 1)


R,C = map(int, input().split())
arr=[list(map(int,input().split())) for i in range(R)]
printdata(arr, 0, 0, R, C)


