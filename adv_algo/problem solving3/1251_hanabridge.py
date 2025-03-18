# 하나로
"""
환경 부담금 = E*L**2
tree...
"""
T = int(input())


def dfs(r, c, cost):

    pass


for test_case in range(1, T + 1):
    # N 섬의 개수
    N = int(input())
    # 각 섬들의 정수인 x좌표
    C = list(map(int, input().split()))
    # 각 섬들의 정수인 y좌표
    R = list(map(int, input().split()))
    # E 환경 부담세율
    E = float(input())

    min_cost = 9e99
    dfs()

    visited = [False] * (N + 1)
    out = [0] * (N + 1)
