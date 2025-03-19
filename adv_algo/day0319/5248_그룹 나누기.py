# 그룹 나누기

T = int(input())


# 특정 원소가 속한 집합 찾기(대표자 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for test_case in range(1, T + 1):
    # N명, M장의 신청서
    N, M = list(map(int, input().split()))
    group = list(map(int, input().split()))

    # 부모 테이블 초기화
    parent = [0] * (N + 1)
    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(1, N + 1):
        parent[i] = i

    # union 연산
    for i in range(M):
        a, b = group[2 * i], group[2 * i + 1]
        union_parent(parent, a, b)

    result = set()
    for i in range(1, N + 1):
        result.add(find_parent(parent, i))

    ans = len(result)

    print(f"#{test_case} {ans}")
