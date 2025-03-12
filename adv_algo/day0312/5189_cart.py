# 전자카트

T = int(input())


def permutaion(idx, cost):
    global visited, out, N, min_cost, arr
    if idx == N:
        # print(out)

        cost += arr[out[N - 1]][0]
        if cost < min_cost:
            min_cost = cost
        return

    # 가지치기. cost 값이 이미 지금까지의 최소값보다 크다면 더이상 볼 필요 없다.
    if cost >= min_cost:
        return

    for n in range(1, N):
        if visited[n] is True:
            continue
        visited[n] = True
        out[idx] = n
        permutaion(idx + 1, cost + arr[out[idx - 1]][n])
        visited[n] = False


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열
    visited = [False] * (N + 1)
    # 결과 저장
    out = [0] * (N + 1)

    # [0,0] 출발
    visited[0] = True
    out[0] = 0
    min_cost = float("inf")

    permutaion(1, 0)

    print(f"#{test_case} {min_cost}")
