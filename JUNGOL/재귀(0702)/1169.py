N,M = map(int, input().split())

dice_list = []
dice_list2 = []
visited_2 = []
visited_3 = [0]*7
def dice(n,m):
    
    # elif len(dice_list2) == n:

    if m==1:
        if len(dice_list) == n:
            print(*dice_list)
            return
        for num in range(1, 7):
            dice_list.append(num)
            dice(n,m)
            dice_list.pop()
    elif m==2:
        if len(dice_list2) == n:
            now = sorted(dice_list2)
            if now not in visited_2:
                visited_2.append(now)
                print(*dice_list2)
                
            return
            
        for num in range(1, 7):
            dice_list2.append(num)
            dice(n,m)
            dice_list2.pop()
    elif m==3:
        if len(dice_list) == n:
            print(*dice_list)
            return
        for num in range(1,7):
            if visited_3[num] == 0:
                dice_list.append(num)
                visited_3[num] = 1
                dice(n,m)
                dice_list.pop()
                visited_3[num] = 0

dice(N,M)