lst = input()
result = 10

for i in range(1,len(lst)):
    if lst[i-1]==lst[i]:
        result += 5
    else:
        result += 10
print(result)
