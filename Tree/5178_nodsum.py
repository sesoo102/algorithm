# 노드의 합
'''
후위 순회
'''

T = int(input())

def post_order(n):
    if n <=N:
        if tree[n] == 0:
            tree[n] = post_order(n*2) + post_order(n*2+1)
        return tree[n]
    else:       # 존재하지 않는 노드일 경우(리프 노드 보다 더 밑으로 갔다면)
        return 0    # 존재하지 않는 노드는 0으로 처리
        

for test_case in range(1, T+1):
    # N 노드의 개수, M 리프 노드의 개수, L 출력할 노드 번호
    N, M, L = list(map(int, input().split()))
    tree = [0] * (N+1)

    for m in range(M):
        node, value = list(map(int, input().split()))
        tree[node] = value

    post_order(1)

    print(f"#{test_case} {post_order(L)}")