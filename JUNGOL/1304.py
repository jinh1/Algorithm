n = int(input())
arr = [[0]*n for _ in range(n)]
num = 0
for i in range(n):
    for j in range(n):
        num += 1
        arr[j][i] = num

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()
