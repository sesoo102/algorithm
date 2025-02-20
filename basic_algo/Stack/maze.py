T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, N):
    visited = [[0]*N for _ in range(N)]

    stack = []
    # 시작점 push
    stack.append((r,c))
    # visited 표시
    visited[r][c] = 1
    # 탐색(while stack)
    while stack:
        r, c = stack.pop()
        if maze[r][c] == '3':
            return 1
        for d in range(4):
            wr, wc = r + dr[d], c +dc[d]
            if 0 <= wr < N and 0<= wc < N and maze[wr][wc] != '1' and visited[wr][wc] == 0:
                stack.append((wr, wc))
                visited[wr][wc] = 1
    return 0

for test_case in range(1, T+1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                sr, sc = r, c
    
    
    ans = dfs(sr, sc, N)

    print(f"#{test_case} {ans}")