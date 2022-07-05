N, M = map(int, input().split())
lst = list(map(int, input().split()))

cut = []
test = []
visited = [0]*N
def rec(n,m):
    if len(cut)==m-1:
        now = sorted(cut)
        
        if now not in test:
            test.append(now)
        
        return 
    
    for i in range(n-1):
        if visited[i] == 0:
            cut.append(i)
            visited[i] = 1
            
            rec(n,m)
            cut.pop()
            visited[i] = 0
        
rec(N,M)
result = []
for t in test:
    now = []
    if len(t)==2:
        result.append(max(sum(lst[:t[0]+1]),
        sum(lst[t[0]+1:t[1]+1]),
        sum(lst[t[1]+1:])))
        # print(sum(lst[t[0]+1:t[1]+1]))
    else:
        for ti in range(len(t)):
            if ti==0:
                now.append(sum(lst[:t[ti]+1]))
            elif ti==len(t)-1:
                now.append(sum(lst[t[ti]+1:]))
            else:
                now.append(sum(lst[t[ti-1]+1:t[ti]+1]))
        result.append(max(now))
    # result.append(max(sum(lst[:t[0]+1]),
    # sum(lst[t[0]+1:t[1]+1]),
    # sum(lst[t[1]+1:])))
    # print(sum(lst[t[0]+1:t[1]+1]))
print(min(result))

