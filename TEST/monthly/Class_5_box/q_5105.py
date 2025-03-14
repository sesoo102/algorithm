# 미로의 거리

"""
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

"""
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