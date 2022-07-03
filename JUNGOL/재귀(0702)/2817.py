# 정렬 되어 있는데 시간초과가 나면 바이너리서치!

N,*numlst = list(map(int, input().split()))

nowlst = []
visited = [0]*N
s_lst = []
def rec(n):
    if len(nowlst) == 6:
        now = sorted(nowlst)       
        if b_search(now):
            s_lst.append(now)    
            print(*now)
        return
    for i in range(N):
        if visited[i] == 0:
            nowlst.append(numlst[i])
            visited[i] = 1
            rec(n)
            nowlst.pop()
            visited[i] = 0

def b_search(mola):
    start = 0
    end = len(s_lst)-1
    while end >= start:        
        middle = (start+end)//2
        target = s_lst[middle]
        for i in range(6):            
            if (target[i] == mola[i]) and (i==5):                
                return False
            elif target[i] > mola[i]:
                end = middle - 1
                break
            elif target[i] < mola[i]:
                start = middle + 1
                break
    return True    
rec(N)
