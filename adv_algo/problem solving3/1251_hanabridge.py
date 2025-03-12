# 하나로
"""
환경 부담금 = E*L**2
"""
T = int(input())


def permutaion(idx):
    global visited, out, N

    if idx == N:
        print(out)
        return

    for n in range(1, N):
        if visited[n] == True:
            continue
        visited[n] = True
        out[idx] = n
        permutaion(idx + 1)
        visited[n] = False


for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    E = float(input())

    # 이거 순열 문제이겠다. 아까 풀었던거 전자카트.

    visited = [False] * (N + 1)
    out = [0] * (N + 1)
