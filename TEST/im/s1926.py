N = int(input())

for n in range(1, N+1):
    num = str(n)

    count = 0
    for i in num:
        if i == '3' or i == '6' or i == '9':
            count += 1
    

    if count > 0:
        print('-'*count, end=' ')
    else:
        print(num, end = ' ')

