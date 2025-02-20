# 노드의 거리

from collections import deque

def bfs(node):
    global adj, V, G
    visited = [0] * (V+1)

    # q 생성
    q = deque()
    # 시작점 인큐
    q.append(node)
    # 시작점 인큐 표시
    visited[node] = 1
    # 탐색
    while q:
        tnode = q.popleft()
        if tnode == G:
            return visited[tnode] - 1
        for i in range(1, V+1):
            if adj[tnode][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[tnode] + 1
                
    return 0


T = int(input())
for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    # 인접 행렬 만들기(V*V의 2차원. 1번부터 시작)
    adj = [[0] * (V+1) for _ in range(V+1)]
    
    # E개 줄에 걸쳐서 간선 입력
    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj[v1][v2] = 1
        adj[v2][v1] = 1
    S, G = list(map(int, input().split()))

    ans = bfs(S)
    print(f'#{test_case} {ans}')