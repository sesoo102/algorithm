# subtree
'''
전위 순회 하면서 subtree 개수 세기
'''

T = int(input())

def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(c1[n])
        pre_order(c2[n])

for test_case in range(1, T+1):
    # E 간선의 개수, N을 루트로 하는 서브 트리에 속한 노드의 개수를 구하여라
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    c1 = [0] * (E + 2)
    c2 = [0] * (E + 2)

    for i in range(E):
        p, c = node[2*i], node[2*i+1]

        # 부모 번호를 인덱스로 자식 번호를 저장
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    cnt = 0
    pre_order(N)
    print(f"#{test_case} {cnt}")