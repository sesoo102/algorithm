# 정사각형 방
from collections import deque

T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):

    cnt = 1
    q = deque()
    q.append((r, c))

    while q:
        sr, sc = q.popleft()

        for d in range(4):
            tr = sr + dr[d]
            tc = sc + dc[d]
            if 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == arr[sr][sc] + 1:
                cnt += 1
                q.append((tr, tc))

    return cnt


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = -1

    for r in range(N):
        for c in range(N):
            cnt = bfs(r, c)
            if max_cnt < cnt:
                max_cnt = cnt
                start_room = arr[r][c]

    print(f"#{test_case} {start_room} {max_cnt}")
