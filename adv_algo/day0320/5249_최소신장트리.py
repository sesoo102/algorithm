# 최소 신장 트리

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


for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    # 간선 정보 저장
    edges = []

    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 같은 집합인지 확인. (union find)
    parents = [p for p in range(V + 1)]  # 정점을 기준으로 make_set

    # 선택한 간선수
    cnt = 0
    # MST 가중치의 합
    mst = 0

    # MST 만들기
    for u, v, w in edges:
        if find_parent(u) != find_parent(v):
            # print(w, u, v)
            union(u, v)
            mst += w
            cnt += 1

            # MST 완성
            if cnt == V:
                break

    print(f"#{test_case} {mst}")
