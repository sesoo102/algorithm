# 탈주범 검거
"""
터널끼리 연결시 이동 가능. 탈주범이 있을 수 있는 위치의 개수 계산
bfs
시간동안 갈 수 있는 최대의 거리들을 구하면 됨. 왔다갔다하는 것은 모두 포함됨.

"""

from collections import deque

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 터널 종류에 따른 이동 가능 방향
types = {
    0: [0, 0, 0, 0],
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}

# 반대 방향을 정의 (0-상, 1-하, 2-좌, 3-우)
reverse_direction = {0: 1, 1: 0, 2: 3, 3: 2}


def bfs(r, c, L, N, M, tunnel):
    queue = deque([(r, c, 1)])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    count = 1

    while queue:
        sr, sc, time = queue.popleft()

        # 탈출 시간이 지나면 종료
        if time >= L:
            continue

        # 현재 위치의 터널 구조 확인
        dirs = types[tunnel[sr][sc]]

        for d in range(4):
            if dirs[d] == 0:
                continue

            tr = sr + dr[d]
            tc = sc + dc[d]
            if 0 <= tr < N and 0 <= tc < M and visited[tr][tc] == 0:
                # 이동하려는 위치의 터널 확인
                next_type = tunnel[tr][tc]
                if next_type == 0:
                    continue

                # 이동할 터널이 현재 터널과 연결되어 있는지 확인
                next_dirs = types[next_type]
                # 반대 방향 연결 확인
                if next_dirs[reverse_direction[d]] == 1:
                    visited[tr][tc] = 1
                    count += 1
                    queue.append((tr, tc, time + 1))

    return count


T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C, L, N, M, tunnel)

    print(f"#{test_case} {ans}")


"""
from collections import deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]

def bfs(r, c):
    global ans
    deq = deque()
    deq.append((r, c))
    time[r][c] = 1

    while deq:
        x, y = deq.popleft()
        ans += 1
        if time[x][y] >= L:
            continue

        for d in range(4):
            if pipe[hole[x][y]][d] == 0:
                continue

            nx, ny = x + dxy[d][0], y + dxy[d][1]
            nd = (d + 2) % 4
            if -1 < nx < N and -1 < ny < M and pipe[hole[nx][ny]][nd] and time[nx][ny] == 0:
                time[nx][ny] = time[x][y] + 1
                deq.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    hole = [list(map(int, input().split())) for _ in range(N)]
    time = [[0 for _ in range(M)] for _ in range(N)]
    ans = 0
    bfs(R, C)
    print('#{} {}'.format(tc, ans))
"""
