# 영역 구하기

M, N, K = map(int, input().split())
# print(M, N, K)
num = []
dr = [0,0,-1,1]
dc = [-1,1,0,0]
field = [[0]*N for _ in range(M)]
# print(field)
for i in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            field[j][k] = 1
cnt = 0
for i in range(M):
    for j in range(N):
        if field[i][j] == 0:
            cnt = 1
            field[i][j] = 1
            queue = [[i, j]]
            while queue:
                r, c = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    x1 = r + dr[k]
                    y1 = c + dc[k]
                    if 0 <= x1 < M and 0 <= y1 < N and field[x1][y1] == 0:
                        field[x1][y1] = 1
                        cnt += 1
                        queue.append([x1, y1])
            num.append(cnt)
num.sort()
print(len(num))
for i in num:
    print(i, end =" ")
# print(field)