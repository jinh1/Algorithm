# 버블정렬
n = int(input())
lst = list(map(int,input().split()))

for i in range(n-1):
    for j in range(n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
    print(*lst)