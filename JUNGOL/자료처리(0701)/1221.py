# 후위표기법1
n = int(input())
lst = input().split()

while 1:
    if len(lst)==1:
        print(int(lst[0]))
        break
    for i in range(len(lst)):
        if lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] == '/':
            now_idx = i          
            break
    
    now_cal = lst.pop(now_idx)
    num_1 = int(lst.pop(now_idx-1))
    num_2 = int(lst.pop(now_idx-2))
    if now_cal == '+':
        lst.insert(now_idx-2,num_1+num_2)
    elif now_cal == '-':
        lst.insert(now_idx-2,num_2-num_1)
    elif now_cal == '*':
        lst.insert(now_idx-2,num_1*num_2)
    elif now_cal == '/':
        lst.insert(now_idx-2,num_2/num_1)
        