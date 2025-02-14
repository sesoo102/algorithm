n = int(input())

for i in range(2*n-1, 1, -2):
    print(' '*((2*n-1-i)//2)+'*'*i)

for i in range(1, 2*n, 2):
    print(' '*((2*n-1-i)//2)+'*'*i)