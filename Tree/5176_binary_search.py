# 이진탐색

T = int(input())

def in_order(n):
    global cnt
    c1 = 2 * n
    c2 = 2 * n + 1

    if c1 <= N:
        in_order(c1)
    tree[n] = cnt
    cnt += 1
    if c2 <= N:
        in_order(c2)

for test_case in range(1, T+1):
    # 노드의 개수
    N = int(input())

    # 완전 이진트리
    tree = [0] * (N+1)
    cnt = 1
    # 루트 노드부터 중위순회
    in_order(1) 

    print(f"#{test_case} {tree[1]} {tree[N//2]}")
