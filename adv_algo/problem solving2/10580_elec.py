# 전봇대
"""
1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
2. 기존의 전선보다 시작점이 낮고, 도착점이 높다다
"""

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    wires = []
    cnt = 0

    for n in range(N):
        A, B = map(int, input().split())
        wires.append([A, B])

        for pre_A, pre_B in wires:
            if pre_A < A and pre_B > B:
                cnt += 1
            if pre_A > A and pre_B < B:
                cnt += 1

    print(f"#{test_case} {cnt}")
