# 장훈이의 높은 선반


def subset(idx, total):
    global min_value

    # 모든 직원 탐색 완료 시
    if idx == N:
        if total >= B:  # B 이상인 경우만 고려
            if total - B < min_value:
                min_value = total - B  # 최소 차이 갱신
        return

    # 현재 원소 포함 X
    subset(idx + 1, total)

    # 현재 원소 포함 O
    subset(idx + 1, total + H[idx])


T = int(input())

for test_case in range(1, T + 1):
    # 직원 수, 선반 높이
    N, B = map(int, input().split())
    # 직원들의 키
    H = list(map(int, input().split()))
    min_value = float("inf")

    # 부분집합 탐색 시작
    subset(0, 0)

    print(f"#{test_case} {min_value}")
