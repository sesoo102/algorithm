import heapq

T = int(input())


def find_parent(x):
    """경로 압축을 적용한 유니온-파인드"""
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    """두 노드를 같은 집합으로 합치는 유니온 연산"""
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a != root_b:
        parent[root_b] = root_a


def kruskal():
    """크루스칼 알고리즘을 이용한 최소 신장 트리 (MST) 계산"""
    edges.sort()  # 비용을 기준으로 오름차순 정렬
    mst_cost = 0
    edge_count = 0

    for cost, u, v in edges:
        if find_parent(u) != find_parent(v):  # 사이클이 발생하지 않으면 추가
            union(u, v)
            mst_cost += cost
            edge_count += 1

            if edge_count == N - 1:  # MST 완성
                break

    return round(mst_cost)  # 최종 결과 반올림


for test_case in range(1, T + 1):
    # N 섬의 개수
    N = int(input())
    # 각 섬들의 정수인 x좌표
    C = list(map(int, input().split()))
    # 각 섬들의 정수인 y좌표
    R = list(map(int, input().split()))
    # E 환경 부담세율
    E = float(input())

    # 좌표 저장
    islands = [(C[i], R[i]) for i in range(N)]

    # 간선 정보 저장 (거리 기반)
    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = islands[i]
            x2, y2 = islands[j]

            # 유클리드 거리의 제곱을 사용하여 가중치 계산
            distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
            cost = distance * E

            # 간선 리스트에 추가 (비용, 노드1, 노드2)
            edges.append((cost, i, j))

    # 유니온-파인드 부모 배열 초기화
    parent = [i for i in range(N)]

    # MST 비용 계산
    ans = kruskal()

    print(f"#{test_case} {ans}")
