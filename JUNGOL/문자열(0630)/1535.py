# lst = list(input().split())
result = []
# for i in range(len(lst)):
#     if i in result:
#         continue
#     else:
#         result.append(lst[i])

while 1:
    words = list(input().split())
    if words[0]=="END":
        break
    for i in words:
        if i in result:
            continue
        else:
            result.append(i)
    real = " ".join(result)
    print(real)

