# 탈주범 검거

T = int(input())

tunnel = {
    "1": [1, 1, 1, 1],
    "2": [1, 1, 0, 0],
    "3": [0, 0, 1, 1],
    "4": [1, 0, 0, 1],
    "5": [0, 1, 0, 1],
    "6": [0, 1, 1, 0],
    "7": [1, 0, 1, 0],
}
for test_case in range(1, T + 1):
    # 세로 가로 r,c 소요된 시간
    N, M, R, C, L = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
