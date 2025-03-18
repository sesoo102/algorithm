def total_synergy(food):
    """팀 내 모든 쌍의 시너지 합산"""
    total = 0
    for i in range(len(food)):
        for j in range(i + 1, len(food)):  # i, j를 조합으로 만들어 합산
            a, b = food[i], food[j]
            total += synergy[a][b] + synergy[b][a]
    return total


def comb(idx, start_i):
    """팀 A와 B를 나누는 DFS 백트래킹"""
    global min_diff

    # food_A를 완성했을 때
    if idx == N // 2:
        food_A = [i for i in range(N) if selected[i]]
        food_B = [i for i in range(N) if not selected[i]]

        # 두 팀의 시너지 차이 계산
        diff = abs(total_synergy(food_A) - total_synergy(food_B))
        min_diff = min(min_diff, diff)
        return

    # 조합 탐색 (index부터 시작하여 중복 방지)
    for i in range(start_i, N):
        if not selected[i]:
            selected[i] = True
            comb(idx + 1, i + 1)
            selected[i] = False  # 백트래킹


# 테스트 케이스 실행
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float("inf")  # 최소 시너지 차이 초기화
    selected = [False] * N  # 음식 조합을 위한 배열

    comb(0, 0)

    print(f"#{test_case} {min_diff}")
