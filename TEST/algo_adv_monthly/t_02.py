import heapq

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nodes = [(0,0)]

    for _ in range(N):
        x, y = map(int, input().split())
        nodes.append((x,y))
    
    visited = [0]* (N+1)
    total_length = 0
    cnt = 0

    pq = []
    pq.append((0,0))    # (거리, 정점번호)

    while pq:
        dist, now = heapq.heappop(pq)

        if visited[now]:
            continue

        visited[now] = 1
        total_length += dist
        cnt += 1

        for nxt in range(N+1):
            if not visited[nxt]:
                x1, y1 = nodes[now]
                x2, y2 = nodes[nxt]
                cost = abs(x1-x2) +abs(y1-y2)
                heapq.heappush(pq, (cost, nxt))
        
        if cnt == N+1:
            break
    
    print(f"#{test_case} {total_length}")