N= int(input())
lst = []
for _ in range(N):
    n = int(input())
    lst.append(n)

result = 0

for i in range(N):
    cnt = 0
    for j in range(i+1,N):
        if lst[i] > lst[j]:
            cnt+= 1
        else:
            break
    result += cnt

print(result)