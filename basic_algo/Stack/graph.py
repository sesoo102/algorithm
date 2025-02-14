T = int(input())

for test_case in range(1, T+1):
    # V: 노드의 개수, E: 간선의 개수.
    # 노드는 섬, 간선은 연결한 선
    V, E = list(map(int, input().split()))
    # V: 정점 갯수, E: 간선 갯수

    # 인접 행렬
    adj =[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        # start, end
        s, e = list(map(int, input().split()))
        adj[s][e] = 1

    # 출발노드, 도착노드
    S, G = list(map(int, input().split()))

    visited = [0] * (V+1)   # 방문표시
    stack = []
    stack.append(S)     # 출발노드 추가
    result = 0

    while stack:
        top = stack[-1]
        # G 도착
        if top == G:
            result = 1
            break

        for i in range(V+1):
            if visited[i] == 0 and adj[top][i] == 1:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    print(f'#{test_case} {result}')
