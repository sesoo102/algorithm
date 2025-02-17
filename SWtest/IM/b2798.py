# 블랙잭

# N장의 카드 M을 넘지 않도록 하는 M과 최대한 가까운 카드 3장의 합
N, M = list(map(int, input().split()))

# 카드
arr = list(map(int, input().split()))

max_value = 0
total = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] +arr[j] +arr[k] <= M:
                total.append(arr[i] +arr[j] +arr[k])

for t in total:
    if max_value < t:
        max_value = t

print(max_value)

