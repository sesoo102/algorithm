# 최소비용
import heapq

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())


def dijkstra():

    pq = []
    heapq.heappush(pq, (arr[0][0], 0, 0))
    dists = [[float("inf")] * N for _ in range(N)]
    dists[0][0] = arr[0][0]

    while pq:
        w, sr, sc = heapq.heappop(pq)

        if sr == N - 1 and sc == N - 1:
            return w

        if w > dists[sr][sc]:
            continue

        for d in range(4):
            tr, tc = sr + dr[d], sc + dc[d]
            if 0 <= tr < N and 0 <= tc < N:
                if arr[sr][sc] > arr[tr][tc]:
                    continue

                new_w = w + arr[tr][tc] - arr[sr][sc] + 1

                if new_w < dists[tr][tc]:
                    dists[tr][tc] = new_w
                    heapq.heappush(pq, (new_w, tr, tc))


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = dijkstra()

    print(f"#{test_case} {ans}")
