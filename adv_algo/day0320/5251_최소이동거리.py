# 최소 이동 거리
import heapq

T = int(input())


def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0))  # (거리합, 시작점)
    dist = [float("inf")] * (N + 1)
    # 시작노드 초기화
    dist[0] = 0

    while pq:
        w, node = heapq.heappop(pq)

        if node == N:
            return w

        if dist[node] < w:
            continue

        for next_info in graph[node]:
            next_w = next_info[1]
            next_node = next_info[0]

            next_w = w + next_w

            if dist[next_node] <= next_w:
                continue

            dist[next_node] = next_w
            heapq.heappush(pq, (next_w, next_node))


for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    ans = dijkstra()

    print(f"#{test_case} {ans}")
