# 입력
c, r = map(int, input().split())
N = int(input())

# 가로(세로로 자르는 선)와 세로(가로로 자르는 선) 분리
cutting_h = [0, r]  # 가로선 (세로 방향 컷)
cutting_v = [0, c]  # 세로선 (가로 방향 컷)

for _ in range(N):
    v, m = map(int, input().split())
    if v == 0:
        cutting_h.append(m)
    else:
        cutting_v.append(m)

# 정렬 (버블 정렬 직접 구현)
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(cutting_h)
bubble_sort(cutting_v)

# 최대 간격 찾기 (직접 구현)
max_h = 0
for i in range(len(cutting_h) - 1):
    diff = cutting_h[i + 1] - cutting_h[i]
    if diff > max_h:
        max_h = diff

max_v = 0
for i in range(len(cutting_v) - 1):
    diff = cutting_v[i + 1] - cutting_v[i]
    if diff > max_v:
        max_v = diff

# 정답 출력
print(max_h * max_v)
