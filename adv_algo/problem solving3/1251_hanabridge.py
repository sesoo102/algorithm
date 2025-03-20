# 하나로
"""
환경 부담금 = E*L**2
tree...
"""
import heapq

T = int(input())


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for test_case in range(1, T + 1):
    # N 섬의 개수
    N = int(input())
    # 각 섬들의 정수인 x좌표
    C = list(map(int, input().split()))
    # 각 섬들의 정수인 y좌표
    R = list(map(int, input().split()))
    # E 환경 부담세율
    E = float(input())

    parent = [p for p in range(N)]
    island = [(C[i], R[i]) for i in range(N)]

    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            d = (C[i] - C[j]) ** 2 + (R[i] - R[j]) ** 2
            edges.append((d, i, j))
    edges.sort()

    cnt = 0
    result = 0
    for d, r, c in edges:
        if find_parent(r) != find_parent(c):
            cnt += 1
            union(r, c)
            result += d * E
            if cnt == N - 1:
                break

    # 소수 첫째 자리에서 반올림하여 정수 형태로 출력
    print(f"#{test_case} {round(result)}")
