# 컨테이너 운반
"""
적재 용량 이하인 것 중 최대값
"""

T = int(input())
for test_case in range(1, T + 1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())

    # 화물 무게
    W = list(map(int, input().split()))
    W.sort(reverse=True)

    # 적재 용량
    T = list(map(int, input().split()))
    T.sort(reverse=True)

    move = 0  # 총 적재한 화물 무게
    # 컨테이너 인덱스
    w_idx = 0

    # 트럭을 순회하면서 적재할 수 있는 가장 무거운 화물을 찾음
    for t in range(M):
        while w_idx < N:
            if T[t] >= W[w_idx]:  # 트럭이 해당 화물을 실을 수 있다면
                move += W[w_idx]  # 적재
                w_idx += 1  # 다음 화물로 이동
                break  # 다음 트럭으로 이동
            w_idx += 1  # 현재 화물을 실을 수 없으면 다음 화물 확인

    print(f"#{test_case} {move}")
