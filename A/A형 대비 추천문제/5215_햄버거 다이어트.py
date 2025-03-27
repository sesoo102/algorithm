# 햄버거 다이어트
"""
조합으로 풀어야하나 싶었는데 부분 집합이 맞겠다....
정해진 칼로리 이하의 조합 중 민기가 가장 선호하는 햄버거 조합
"""


def subset(idx, sub):
    global total

    if idx == N:
        total_score = 0
        total_cal = 0
        for i in range(len(sub)):
            total_score += sub[i][0]
            total_cal += sub[i][1]
        total.append((total_score, total_cal))
        return

    # 현재 원소 포함
    subset(idx + 1, sub + [ingredient[idx]])

    # 현재 원소 포함 x
    subset(idx + 1, sub)


T = int(input())
for test_case in range(1, T + 1):
    # N 재료의 수, L 제한 칼로리
    N, L = list(map(int, input().split()))
    ingredient = []
    for _ in range(N):
        score, cal = map(int, input().split())
        ingredient.append((score, cal))
    # print(ingredient)
    # print(ingredient[0])
    total = []
    subset(0, [])

    max_value = -1

    # print(total)

    for s, c in total:
        if c <= L:
            max_value = max(max_value, s)

    print(f"#{test_case} {max_value}")
