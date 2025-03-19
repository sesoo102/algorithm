# 보급로

from collections import deque

# 상하좌우 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def repair():
    INF = 999999  # 충분히 큰 값
    min_time = [[INF] * N for _ in range(N)]  # 최소 복구 시간을 저장할 배열
    min_time[0][0] = 0  # 시작점 초기화

    # `deque`를 사용한 "우선순위 큐" 구현 (비용이 적은 순으로 정렬 유지)
    q = deque()
    q.append((0, 0, 0))  # (누적 복구 시간, r, c)

    while q:
        # 현재 탐색할 좌표 중 최소 비용을 가진 노드를 `deque`에서 꺼냄
        q = deque(sorted(q))  # 비용 기준으로 정렬 (heapq 대체)
        s_time, sr, sc = q.popleft()

        # 목표 지점(N-1, N-1)에 도달하면 최소 시간 반환
        if sr == N - 1 and sc == N - 1:
            return s_time

        for d in range(4):
            tr, tc = sr + dr[d], sc + dc[d]
            if 0 <= tr < N and 0 <= tc < N:
                new_time = s_time + arr[tr][tc]

                # 기존보다 더 빠른 경로라면 갱신하고 `deque`에 추가
                if new_time < min_time[tr][tc]:
                    min_time[tr][tc] = new_time
                    q.append((new_time, tr, tc))


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [
        list(map(int, list(input()))) for _ in range(N)
    ]  # 한 줄씩 입력받아 숫자로 변환

    result = repair()
    print(f"#{test_case} {result}")
