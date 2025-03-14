# 격자판의 숫자 이어 붙이기

T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, number):
    if len(number) == 7:
        number_set.add(number)
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, number + arr[nr][nc])


for test_case in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    number_set = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, arr[r][c])

    print(f"#{test_case} {len(number_set)}")
