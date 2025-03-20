# 햄버거 다이어트


def comb(idx, start_i):
    global total_cal, total_score, total
    if idx == R:
        for i in range(N):
            if selected[i]:
                total.append((sum(ingredient[i][0]), sum(ingredient[i][1])))
        return
    for i in range(start_i, N):
        if not selected[i]:
            selected[i] = True
            comb(idx + 1, i + 1)
            selected[i] = False


T = int(input())
for test_case in range(1, T + 1):
    # N 재료의 수, L 제한 칼로리
    N, L = int(input().split())
    ingredient = []
    for _ in range(N):
        score, cal = map(int, input().split())
        ingredient.append((score, cal))

    selected = [False] * N
    R = [r for r in range(1, N + 1)]

    total_score = total_cal = 0
    total = []

    max_value = -1
    for s, c in total:
        if c <= L:
            max_value = max(max_value, s)

    print(f"#{test_case} {max_value}")
