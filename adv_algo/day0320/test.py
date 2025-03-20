# 부모찾는 함수
def Find(n):
    # 부모가 자신이 아니라면
    if parent[n] != n:
        # 부모 찾기
        parent[n] = Find(parent[n])
    return parent[n]


# 부모관계 설정하는 함수
# 기본 값은 자기자신으로 되어있으므로 간선을 입력 받을 때마다 관계 설정하기
def union(a, b):
    # 부모 찾기
    a = Find(a)
    b = Find(b)
    # 부모가 작은 쪽을 부모로 두고 값을 변경
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for test_case in range(1, T + 1):
    # V: 마지막 노드 번호, E: 간선의 개수
    V, E = map(int, input().split())
    # 간선 정보 리스트
    relation = [0] * (E)
    # 가중치를 기준으로 정렬해야 하므로 가중치를 첫번쨰로 입력한 간선 정보를 입력하기
    for i in range(E):
        # n1, n2: 양 끝 노드 번호 , w: 가중치
        n1, n2, w = map(int, input().split())
        relation[i] = [w, n1, n2]
    relation.sort()
    # 부모 테이블 생성 (기본 값은 자기자신)
    parent = list(range(V + 1))
    # 최소값
    mn = 0
    # 연결이 모두 끝났을 경우 멈추기 위한 cnt
    # 간선 개수 - 1이라면 모두 연결된 것
    cnt = 0
    for i in range(E):
        w, n1, n2 = relation[i]
        # n1과 n2가 부모가 같은지 확인
        # 다르다면 union함수로 n1과 n2를 연결해주기
        if Find(n1) != Find(n2):
            print(f"집합 {w}, {n1}, {n2}")
            union(n1, n2)
            # 가중치 더하기
            mn += w
            cnt += 1
        # 모두 연결되었다면 break로 종료
        if cnt >= V:
            break

    print(f"#{test_case} {mn}")
