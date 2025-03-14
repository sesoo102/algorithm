# 이진탐색
'''
이진 탐색 트리. LVR 중위순회
'''

T = int(input())


def in_order(n):
    # i 는 중위 순회할 때 1부터 N까지 증가하는 숫자를 저장하는 역할.
    # i를 전역 변수로 선언해야, 함수 호출이 중첩될 때도 값이 유지되며 증가한다.
    # 만약 global i를 사용하지 않으면, 재귀 호출될 때 i가 계속 초기화되어 원하는 값이 저장되지 않는다.
    global i
    if N >= n:      
        in_order(n * 2)
        # V
        tree[n] = i
        i += 1
        in_order(n * 2 + 1)





for test_case in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    i = 1
    in_order(1)


    print(f"#{test_case} {tree[1]} {tree[N//2]}")