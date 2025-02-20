# 미로1
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    visited = [[0]*16 for _ in range(16)]

    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q:
        tr, tc = q.popleft()
        if maze[tr][tc] == '3':
            return 1

        for d in range(4):
            wr = tr + dr[d]
            wc = tc + dc[d]
            if 0 <= wr < 16 and 0 <= wc < 16 and maze[wr][wc] != '1' and visited[wr][wc] == 0:
                q.append((wr, wc))
                visited[wr][wc] = 1
    return 0

for test_case in range(1, 11):
    input()
    maze = [list(input().strip()) for _ in range(16)]

    # 출발점
    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                sr, sc = r, c
            
    ans = bfs(sr, sc)

    print(f"#{test_case} {ans}")
