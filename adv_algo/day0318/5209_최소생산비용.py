# visited 를 2차원으로 만들었더니 시간초과가 나온다....

T = int(input())


def check(row, col):
    # 같은 열에 이미 방문한 적이 있는지 확인
    for i in range(row):
        if visited[i][col]:  # 위쪽 행에서 같은 열(col)을 선택한 적 있으면 False
            return False

    return True


def min_price(row, total):
    global min_value

    if total >= min_value:
        return

    if row == N:
        min_value = min(min_value, total)
        return

    # 각 행(row)에서 가능한 열(col) 선택
    for col in range(N):
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        min_price(row + 1, total + arr[row][col])
        visited[row][col] = 0


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    min_value = 99999999
    min_price(0, 0)

    print(f"#{test_case} {min_value}")
