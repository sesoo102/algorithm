# 롤케이크 길이 L
L = int(input())
# 방청객 수 N
N = int(input())

# 롤케이크 조각 상태 (1~L번까지 존재)
arr = [0] * (L + 1)

# 각 방청객이 실제로 받은 조각 수
cnt = [0] * (N + 1)
e_ans = [0] * (N + 1)  # 기대한 조각 개수

# 예상 조각 개수 저장 및 롤케이크 분배
for i in range(1, N + 1):
    P, K = map(int, input().split())
    e_ans[i] = K - P + 1  # 예상 조각 저장

    # 롤케이크 배분
    for j in range(P, K + 1):
        if arr[j] == 0:  # 아직 배정되지 않은 조각만 할당
            arr[j] = i

# 실제 받은 조각 개수 계산
for j in range(1, L + 1):
    if arr[j] != 0:
        cnt[arr[j]] += 1

# 가장 기대가 컸던 방청객 찾기
max_eidx = 1
for i in range(2, N + 1):  # 1번부터 비교
    if e_ans[max_eidx] < e_ans[i]:
        max_eidx = i

# 실제로 가장 많은 조각을 받은 방청객 찾기
max_idx = 1
for i in range(2, N + 1):  # 1번부터 비교
    if cnt[max_idx] < cnt[i]:
        max_idx = i

print(max_eidx)
print(max_idx)
