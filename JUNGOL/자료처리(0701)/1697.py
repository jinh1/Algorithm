# 큐
n = int(input())
queue = []
for i in range(n):
    words = input().split()
    if words[0]=='i':
        queue.append(words[1])
    elif words[0]=='c':
        print(len(queue))
    elif words[0]=='o':
        if len(queue)==0:
            
            print('empty')
        else:
            print(queue.pop(0))