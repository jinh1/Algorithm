N = int(input())
nlst = list(map(int, input().split()))
M = int(input())
mlst = list(map(int, input().split()))

def b_search(lst,target):
    start = 0
    end = len(lst)-1
    
    while start <= end:
        middle = (start+end)//2
        if lst[middle] == target:
            return middle
        if lst[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1


for num in mlst:
    print(b_search(nlst,num), end = " ")
