# 창고 다각형

N = int(input())

pillars = []
result = 0
for i in range(N):
    L, H = map(int, input().split())
    pillars.append([L, H])

# 버블 정렬을 이용한 정렬 (내장 함수 sort() 대체)
for i in range(N - 1):
    for j in range(N - 1 - i):
        if pillars[j][0] > pillars[j + 1][0]:
            pillars[j], pillars[j + 1] = pillars[j + 1], pillars[j]

# 가장 높은 기둥 찾기 (내장 함수 max() 대체)
max_height = 0
idx = 0
for i in range(N):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        idx = i

# 초기 높이는 첫 번째 기둥의 높이
height = pillars[0][1]

# 최대 높이전까지 면적 계산
for i in range(idx):
    if height < pillars[i + 1][1]:
        result += height * (pillars[i + 1][0] - pillars[i][0])
        height = pillars[i + 1][1]
    else:
        result += height * (pillars[i + 1][0] - pillars[i][0])

# 최대 높이 기둥의 면적 추가
result += max_height

# 뒤에서부터도 똑같이 진행
height = pillars[-1][1]

for i in range(N - 1, idx, -1):
    if height < pillars[i - 1][1]:
        result += height * (pillars[i][0] - pillars[i - 1][0])
        height = pillars[i - 1][1]
    else:
        result += height * (pillars[i][0] - pillars[i - 1][0])

print(result)
