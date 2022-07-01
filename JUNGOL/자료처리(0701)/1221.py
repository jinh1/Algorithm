# 후위표기법1
n = int(input())
lst = input().split()
number = []
cal = []

for _ in range(n):
    now = lst.pop(0)
    if now != '+' and now != '-' and now != '*' and now != '/':
        number.append(int(now))
    else:
        cal.append(now)
result = number.pop(0)
while len(cal) != 0:
    n_cal = cal.pop(0)
    if n_cal == '+':
        result += number.pop(0)
    elif n_cal == '-':
        result -= number.pop(0)
    elif n_cal == '*':
        result *= number.pop(0)
    elif n_cal == '/':
        result /= number.pop(0)
        result = int(result)
print(result)
