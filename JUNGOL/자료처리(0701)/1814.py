# 삽입정렬, 이동횟수 출력
n = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in range(1, n):
    for j in range(i,0,-1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            cnt+=1

print(cnt)