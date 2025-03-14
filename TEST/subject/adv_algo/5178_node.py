# 노드의 합

'''
리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력
 # >>> 후위순회(post_order) LRV
'''

T = int(input())

def post_oder(n):
    if n <= N:
        if tree[n] == 0:
            left = post_oder(n * 2)
            right = post_oder(n * 2 + 1)
            tree[n] = left + right
        return tree[n]

    # 노드가 없으면 0 반환
    # (자식 노드가 없을 경우에 0을 반환하여 오류 방지, 이진 트리의 경우 자식 노드가 없을 수 있으므로 꼭 필요)
    # 이문제에선 완전 이진 트리임으로 없어도 동작 가능, but 예외상황 방지를 위해 작성하는 것이 안전함
    return 0



for test_case in range(1, T+1):
    # N 노드의 개수, M leaf 노드의 개수, L 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 완전 이진 트리래. >> 트리를 우선 만들자
    tree = [0] * (N+1)
    for m in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    post_oder(1)

    print(f'#{test_case} {post_oder(L)}')

