lst = input()
k_cnt = 0
i_cnt = 0

for i in range(len(lst)-2):
    if lst[i]=='K':
        if lst[i+1]=='O':
            if lst[i+2]=='I':
                k_cnt += 1

for i in range(len(lst)-2):
    if lst[i]=='I':
        if lst[i+1]=='O':
            if lst[i+2]=='I':
                i_cnt += 1

print(k_cnt)
print(i_cnt)