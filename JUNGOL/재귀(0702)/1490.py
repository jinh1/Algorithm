N, K = map(int, input().split())
target = list(map(int, input().split()))
# print(N, K)
# print(target)
c_list = []
now_list = []
visited = [0]*(N+1)
def rec(n, k):
    if len(now_list) == k:
        now = sorted(now_list)
        flag = 1
        for list in c_list:
            if list == now:
                flag = 0

        if flag:
            c_list.append(now)
    for num in range(1,n+1):
        if visited[num] == 0:
            now_list.append(num)
            visited[num] = 1
            rec(n,k)
            now_list.pop()
            visited[num] = 0
rec(N,K)
for lst_idx in range(len(c_list)):
    if c_list[lst_idx] == target:
        target_idx = lst_idx
        break
if target_idx == (len(c_list)-1):
    print('NONE')
else:
    print(*c_list[target_idx+1])
