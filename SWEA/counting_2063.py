N = int(input())
arr = list(map(int, input().split()))

# 최대값 찾기 없이 배열 크기를 정할 수 없으므로, 주어진 숫자의 범위를 미리 안다면 max 없이 가능
max_value = 0
for num in arr:  # 최대값 찾기 (sum, max 사용 금지)
    if num > max_value:
        max_value = num

# Step 1: 카운팅 배열 초기화
count = [0] * (max_value + 1)

# Step 2: 숫자 등장 횟수 세기
for num in arr:
    count[num] += 1

# Step 3: 정렬된 결과를 담을 배열 생성
sorted_arr = []

# Step 4: 카운팅 배열을 순회하며 정렬된 값 저장
for i in range(len(count)):
    for _ in range(count[i]):
        sorted_arr.append(i)

# 중앙값 찾기
middle = N // 2
print(sorted_arr[middle])