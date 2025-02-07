T = int(input())

for test_case in range(1, T+1):
    # N * N 배열, M * M 크기의 파리채
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 처음 위치 (r, c)

