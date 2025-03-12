# 최소합

from collections import deque

# 우하
dr = [0, 1]
dc = [1, 0]


def bfs(r, c):
    visited = [[float("inf")] * N for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = arr[r][c]

    while q:
        sr, sc = q.popleft()

        if sr == N - 1 and sc == N - 1:
            return visited[sr][sc]

        for d in range(2):
            tr = sr + dr[d]
            tc = sc + dc[d]

            # 범위 체크
            if 0 <= tr < N and 0 <= tc < N:
                # 최소합
                min_value = visited[sr][sc] + arr[tr][tc]

                # 최소합이라면 갱신후 인큐
                if min_value < visited[tr][tc]:
                    visited[tr][tc] = min_value
                    q.append((tr, tc))


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(0, 0)
    print(f"#{test_case} {ans}")
