n = int(input())
# n 번째 줄에 2n -1

for i in range(1, 2*n, 2):
    print(' '*((2*n - 1 - i)//2) + '*'*i)