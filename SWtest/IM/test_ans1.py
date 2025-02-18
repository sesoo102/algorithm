# dfs 스택 활용
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs_stack(r, c):
    global max_count
    stack = [(r, c, 1)]  # 스택 초기화: (현재 행, 현재 열, 이동 횟수)

    while stack:
        r, c, count = stack.pop()

        # 최소값 찾기
        min_value = arr[r][c]
        next_r, next_c = -1, -1

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] < min_value:  # 최소값 찾기
                    min_value = arr[nr][nc]
                    next_r, next_c = nr, nc

        # 이동할 곳이 있다면 스택에 추가
        if next_r != -1 and next_c != -1:
            stack.append((next_r, next_c, count + 1))
        else:
            # 최댓값 갱신 (max 사용 X)
            if count > max_count:
                max_count = count

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for r in range(N):
        for c in range(N):
            dfs_stack(r, c, 1)  # 시작 위치에서 길이 1부터 시작

    print(f'#{test_case} {max_count}')