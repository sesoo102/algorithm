# 수영장


def dfs(month, cost):
    global min_cost

    # 12개월을 넘으면 최소 비용 업데이트
    if month > 12:
        if min_cost > cost:
            min_cost = cost
        return

    # 이미 계산된 최소 비용보다 크다면 가지치기
    if cost >= min_cost:
        return

    # 1일 이용권
    dfs(month + 1, cost + plan[month] * D)

    # 1달 이용권
    dfs(month + 1, cost + M)

    # 3달 이용권
    dfs(month + 3, cost + T)

    # 1년 이용권 (한 번만 사용하면 되므로 DFS 밖에서 체크 가능)


T = int(input())

for test_case in range(1, T + 1):
    # 요금제 입력 (1일권, 1달권, 3달권, 1년권)
    D, M, T, Y = map(int, input().split())

    # 각 달별 이용 계획 (1~12월)
    plan = [0] + list(map(int, input().split()))  # 0번째는 더미 (1-based index)

    # 최소 비용 초기화 (1년 이용권부터 시작)
    min_cost = Y

    # DFS 탐색 시작
    dfs(1, 0)

    print(f"#{test_case} {min_cost}")
