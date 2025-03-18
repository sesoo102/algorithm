T = int(input())


def min_price(row, total):
    global min_value

    if total > min_value:
        return

    if row == N:
        min_value = min(min_value, total)
        return

    for col in range(N):
        if visited[col] == 1:
            continue

        visited[col] = 1
        min_price(row + 1, total + arr[row][col])
        visited[col] = 0


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_value = 999999999

    min_price(0, 0)

    print(f"#{test_case} {min_value}")
