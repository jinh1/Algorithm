n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
if m==1:
    for i in range(n):
        for j in range(n):
            arr[i][j] = i+1

elif m==2:
    for i in range(n):
        if i%2==0:
            for j in range(n):
                arr[i][j] = j+1
        else:
            for j in range(n):
                arr[i][j] = n-j

elif m==3:
    for i in range(n):
        for j in range(n):
            arr[i][j] = 1+i+j+(i*j)

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()