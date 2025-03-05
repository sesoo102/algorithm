# 수 이어가기

N = int(input())

ans = []
max_len = 0
for i in range(1, N+1):
    temp = [N, i]
    while temp[-1] >= 0:
        temp.append(temp[-2] - temp[-1])
    temp.pop()

    if max_len < len(temp):
        max_len = len(temp)
        ans = temp
    
print(max_len)
print(*ans)