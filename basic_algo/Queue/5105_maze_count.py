# 미로의 거리

from collections import deque

T = int(input())

# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs
def bfs(r, c, N):
    # visited 생성
    visited = [[0]*N for _ in range(N)]

    # q 생성
    q = deque()
    # 시작점 인큐
    q.append((r,c))
    # 시작점 인큐 표시
    visited[r][c] = 1
    # 탐색 (while q)
    while q:
        tr, tc = q.popleft()
        if maze[tr][tc] == '3':
            # 도착점일때 visited의 값 - 첫번째 - 1(문제조건이 이렇다. 출발 도착 제외 빈칸수)
            return visited[tr][tc] -1 -1
        for d in range(4):
            wr, wc = tr + dr[d], tc + dc[d]
            # 미로 내부 and 벽이 아니다 and 방문한적이 없다.
            if 0 <= wr < N and 0 <= wc < N and maze[wr][wc] != '1' and visited[wr][wc] == 0:
                q.append((wr, wc))
                visited[wr][wc] = visited[tr][tc] + 1
    return 0

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                sr, sc = r, c
    
    ans = bfs(sr, sc, N)
    print(f'#{test_case} {ans}')