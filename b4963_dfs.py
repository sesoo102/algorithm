dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

def dfs(r, c):
    
    stack = []
    stack.append((r,c))
    visited[r][c] = 1

    while stack:
        sr, sc = stack.pop()
        for d in range(8):
            ar, ac = sr +dr[d], sc + dc[d]
            if 0 <= ar < h and 0<= ac <w and sea_map[ar][ac] != 0 and visited[ar][ac] == 0:
                stack.append((ar, ac))
                visited[ar][ac] = 1


while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break

    sea_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]


    island_count = 0
    for r in range(h):
        for c in range(w):
            if sea_map[r][c] == 1 and visited[r][c] == 0:
                dfs(r, c)
                island_count += 1
    
    print(island_count)


    # 재귀
    import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정 (필요 시 추가)

dr = [-1, 1, 0, 0, -1, 1, -1, 1]  # 8방향 (상, 하, 좌, 우, 대각선)
dc = [0, 0, -1, 1, 1, 1, -1, -1]

def dfs(r, c):
    visited[r][c] = 1  # 방문 처리

    for d in range(8):  # 8방향 탐색
        ar, ac = r + dr[d], c + dc[d]
        if 0 <= ar < h and 0 <= ac < w and sea_map[ar][ac] == 1 and visited[ar][ac] == 0:
            dfs(ar, ac)  # 재귀 호출

while True:
    w, h = map(int, input().split())  # 너비, 높이 입력
    if w == 0 and h == 0:
        break  # 종료 조건

    sea_map = [list(map(int, input().split())) for _ in range(h)]  # 지도 입력
    visited = [[0] * w for _ in range(h)]  # 방문 배열

    island_count = 0
    for r in range(h):
        for c in range(w):
            if sea_map[r][c] == 1 and visited[r][c] == 0:
                dfs(r, c)  # 새로운 섬 발견 시 DFS 탐색 시작
                island_count += 1  # 섬 개수 증가

    print(island_count)

