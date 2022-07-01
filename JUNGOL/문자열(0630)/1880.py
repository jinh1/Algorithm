key = input()
lst = input()

result = ''

for i in range(len(lst)):
    if lst[i] ==" ":
        result+=" "
    elif ord(lst[i])>= 65 and ord(lst[i])<=90:
        result+=(key[int(ord(lst[i].lower())-97)].upper())
        # print(key[ord(lst[i].lower()-97)].upper())
    else:
        result+=(key[int(ord(lst[i])-97)])
print(result)