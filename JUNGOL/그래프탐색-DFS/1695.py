N = int(input())
field = [list(input()) for _ in range(N)]
num = []
# print(field)

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def dfs(r,c):
    if r<0 or r>=N or c<0 or c>=N:
        return False
    if field[r][c] == '1':
        global cnt
        cnt += 1
        field[r][c] = 0 
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            dfs(nr,nc)
        return True
    return False
cnt = 0

for i in range(N):
    for j in range(N):
        if dfs(i,j):
            num.append(cnt)
            cnt = 0
num.sort()
print(len(num))
for i in num:
    print(i)