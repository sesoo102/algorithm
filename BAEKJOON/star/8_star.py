n = int(input())

# 상단 피라미드
for i in range(n-1):
    print('*'*(i+1) + ' '*(2*(n-i-1)) + '*'*(i+1))

# 하단 역피라미드
for i in range(n-1, -1, -1):
    print('*'*(i+1) + ' '*(2*(n-i-1)) + '*'*(i+1))
