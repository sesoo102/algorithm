# 이진 힙
'''
    # 힙의 삽입 연산
    # 최소 힙, 최대 힙은 완전 이진 트리. >> 배열로 트리 저장
    # last 변수 선언 해서 현재 트리의 마지막 노드 인덱스 추적하기.
    # 힙의 가장 마지막에 노드(last + 1)를 집어 넣는다.
    # 새로 추가된 노드를 자식 노드로 하고, 부모 노드와 비교
    #   - 만약, 부모가 더 큰 경우(최소 힙에 위배되는 경우)
    #      - 부모 <=> 자식
    #      - 부모를 자식으로 놓고, 새로운 부모와 계속 비교를 해 나간다.
    #      - 루트 노드와 비교하면 끝.
    #   - 만약, 부모 <= 자식 (최소힙의 규칙에 맞는 경우)
    #      - 그냥 종료

'''

T = int(input())

def enque(n):
    global last
    last += 1
    heap[last] = n

    # 부모 자식 비교
    c = last
    p = last // 2
    # 부모가 존재 and 부모가 자식 보다 작을때까지 위치 교환
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 기존 부모 노드를 자식 노드로 변경
        c = p
        p = c // 2


for test_case in range(1, T+1):
    # 노드의 개수. (마지막 노드의 번호)
    N = int(input())
    value = list(map(int, input().split()))

    heap = [0] * (N+1)
    # 마지막 노드 인덱스
    last = 0

    # 문제에서 주어진 값들 완전 이진트리에 최소힙으로 저장
    for v in value:
        enque(v)


    ans = 0
    # i 마지막 노드의 부모 노드
    i = N // 2
    while i >= 1:
        ans += heap[i]
        i = i // 2

    print(f"#{test_case} {ans}")