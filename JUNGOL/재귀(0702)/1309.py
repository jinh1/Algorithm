n = int(input())
result = 1
def fac(num):
    global result
    if num != 1:
        print(f'{num}! = {num} * {num-1}!')
        result *= num
        return fac(num-1)
    else:
        print("1! = 1")
        print(result)
fac(n)