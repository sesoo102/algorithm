my_list = []

# 10개의 수를 입력받고, 42로 나눈 나머지를 리스트에 저장
for i in range(10):
    n = int(input())
    my_list.append(n % 42)

cnt = [0] * 42  # 나머지 값을 카운트할 리스트

# 나머지 값이 나온 횟수를 저장
for num in my_list:
    cnt[num] += 1

# 0부터 41까지 다른 나머지 개수를 세기
count = 0
for j in range(42):  # 0부터 41까지 검사해야 함
    if cnt[j] != 0:
        count += 1

# 결과 출력
print(count)
