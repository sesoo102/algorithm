from collections import deque

# 상하좌우 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# BFS 함수
def bfs(r, c):
    q = deque([(r, c)])  # 큐 초기화
    count = 1  # 이동할 수 있는 방 개수 (시작점 포함)

    while q:
        sr, sc = q.popleft()

        for d in range(4):
            tr = sr + dr[d]
            tc = sc + dc[d]

            if 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == arr[sr][sc] + 1:
                q.append((tr, tc))
                count += 1  # 이동 가능한 방 개수 증가

    return count


T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # 방의 크기 (N x N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0  # 최대 이동할 수 있는 방 개수
    start_room = float("inf")  # 이동이 가장 긴 방의 시작 번호

    # 모든 방에서 BFS 수행
    for r in range(N):
        for c in range(N):
            count = bfs(r, c)  # 해당 위치에서 BFS 실행

            # 가장 긴 이동 경로 찾기 (이동 개수가 같다면 시작 번호가 작은 것 선택)
            if count > max_count or (count == max_count and arr[r][c] < start_room):
                max_count = count
                start_room = arr[r][c]

    print(f"#{test_case} {start_room} {max_count}")
