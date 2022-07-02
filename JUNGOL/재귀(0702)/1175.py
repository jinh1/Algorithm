N,M = map(int, input().split())

num_list = []
def dice(n,m):
    if len(num_list) == n and sum(num_list) == m:
        print(*num_list)
        return
    elif len(num_list) == n:
        return
    
    for num in range(1,7):
        num_list.append(num)
        dice(n,m)
        num_list.pop()

dice(N,M)