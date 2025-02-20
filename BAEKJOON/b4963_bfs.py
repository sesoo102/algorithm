# 섬의 개수 bfs
# 1 땅, 0 바다
from collections import deque

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

def bfs(r, c):
    
    q = deque()
    q.append((r,c))
    visited[r][c] = 1

    while q:
        sr, sc = q.popleft()
        for d in range(8):
            ar = sr + dr[d]
            ac = sc + dc[d] 
            if 0 <= ar < h and 0 <= ac < w and sea_map[ar][ac] != 0 and visited[ar][ac] == 0:
                q.append((ar, ac))
                visited[ar][ac] = 1



while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break

    sea_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    
    island_count = 0
    # 출발 위치 
    for r in range(h):
        for c in range(w):
            if sea_map[r][c] == 1 and visited[r][c] == 0:
                bfs(r, c)
                island_count += 1
    
    print(island_count)