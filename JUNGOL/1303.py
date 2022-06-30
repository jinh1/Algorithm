n, m = map(int,input().split())
arr = [[0]*m for _ in range(n)]

num = 0
for i in range(n):
    if i%2==0:
        for j in range(m):
            num += 1
            arr[i][j] = num
            
    else:
        for k in range(m-1,-1,-1):
            num += 1
            arr[i][k] = num
           


for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()