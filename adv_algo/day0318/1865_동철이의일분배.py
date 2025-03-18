# 동철이의 일 분배

T = int(input())


def best(row, ans):
    global max_value

    if ans <= max_value:
        return

    if row == N:
        max_value = max(max_value, ans)
        return

    for col in range(N):
        if visited[col] == 1:
            continue

        visited[col] = 1
        best(row + 1, ans * (arr[row][col] / 100))
        visited[col] = 0


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    max_value = -1
    best(0, 1)

    print(
        f"#{test_case} {max_value*100:.6f}"
    )  # 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력
