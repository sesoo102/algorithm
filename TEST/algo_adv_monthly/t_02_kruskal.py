T = int(input())

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    # 사이클 방지
    if a == b:
        return

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for test_case in range(1, T+1):
    N = int(input())
    nodes = [(0,0)]

    for _ in range(N):
        x, y = map(int, input().split())
        nodes.append((x,y))
    
    edges = []

    # 간선 만들기
    for i in range(N+1):
        for j in range(i,N+1):
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]
            cost = abs(x1-x2)+abs(y1-y2)
            edges.append((cost, i, j))
    
    edges.sort()

    parents = [p for p in range(N+1)]
    total = 0
    cnt =0

    for cost, u, v in edges:
        if find_parent(u) != find_parent(v):
            union(u, v)
            total += cost
            cnt += 1
            if cnt == N:
                break
    
    print(f"#{test_case} {total}")