# 벽돌깨기
"""
0은 빈 공간, 그 외의 숫자는 벽돌
구슬은 좌, 우
벽돌 1~9
구슬이 명중한 벽돌은 상하좌우로(벽돌에 적힌 숫자 - 1)칸 만큼 같이 제거
최대한 많은 벽돌 제거
남은 벽돌의 개수 구하기
"""

from collections import deque

T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 구슬을 조준하는 벽돌 찾기
def shooting_marble(r, c):
    visited = [[0] * W for _ in range(H)]
    stack = []
    time = 0
    stack.append([r, c, time])
    visited[r][c] = 1

    while stack:
        tr, tc, s_time = stack.pop()
        if time > N:
            continue

        if arr[tr][tc] != 0:
            visited[tr][tc] = 1
            return tr, tc

        for d in range(4):
            fr = tr + dr[d]
            fc = tc + dc[d]
            if 0 <= fr < N and 0 <= fc < N and visited[fr][fc] == 0:
                s_time += 1
                visited[fr][fc] = 1
                stack.append([fr, fc, s_time])


# 연쇄작용
def bomb(r, c):
    visited = [[0] * N for _ in range(N)]

    brick_break_cnt = arr[r][c]
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        sr, sc = q.popleft()
        for d in range(4):
            for m in range(arr[sr][sc]):
                tr = sr + dr[d] * m
                tc = sc + dc[d] * m
                if 0 <= tr < N and 0 <= tc < N and visited[tr][tc] == 0:
                    brick_break_cnt += arr[tr][tc]
                    visited[tr][tc] = visited[sr][sc] + 1
                    q.append([tr, tc])

                    # 중력작용
                    for j in range(W):
                        idx = H - 1
                        for i in range(H - 1, -1, -1):
                            if arr[i][j]:
                                arr[i][j], arr[idx][j] = arr[idx][j], arr[i][j]
                                idx -= 1

    return brick_break_cnt


for test_case in range(1, T + 1):
    # N 구슬 쏠 수 있는 횟수, W*H
    N, W, H = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(H)]

    for r in range(H):
        for c in range(W):
            sc = c

    fr, fc = shooting_marble(0, sc)
    result = bomb(fr, fc)

    b_cnt = 0
    for row in arr:
        for el in row:
            if el:
                b_cnt += 1

    ans = b_cnt - result

    print(f"#{test_case} {ans}")
