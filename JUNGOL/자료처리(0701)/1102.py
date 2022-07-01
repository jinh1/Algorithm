# 스택
n = int(input())
stack = []
for i in range(n):
    words = list(input().split())
    if words[0] =='i':
        stack.append(int(words[1]))
    elif words[0] == 'c':
        print(len(stack))
    elif words[0] == 'o':
        if len(stack) == 0:
            print('empty')
        else:
            print(stack.pop())

