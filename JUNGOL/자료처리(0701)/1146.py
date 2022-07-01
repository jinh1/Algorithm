# 선택정렬
n = int(input())
lst = list(map(int,input().split()))

for i in range(n-1):
    # tgt = lst
    mim = 101
    idx = 101
    
    for j in range(i,n):
        if mim > lst[j]:
            mim = lst[j]
            idx = j
    
    lst[idx] = lst[i]
    lst[i] = mim
    print(*lst)
    