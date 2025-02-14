n = int(input())

for i in range(2*n-1):
    if i <= n:
        for j in range(2*n):
            print('*'*(j+1) + ' '*(2*n -2*(j+1)) + '*'*(j+1))
    else:
        for j in range(2*n):
            print('*'*(n -(j+1)) + ' '*(2*(j+1)) + '*'*(n -(j+1)))