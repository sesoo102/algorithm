# 등산로 조성
"""
가장 높은 곳이 정상
같은 높이 이동불가. 정상 기준으로 계속 작은 값만
지형의 높이가 1보다 작게 만들어 깍을 수 있다.
가장 긴 등산로의 길이
"""
# from collections import deque

T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, length, used):
    global max_len

    # if length == 1:
    #     print(arr[r][c], r, c)

    if length > max_len:
        max_len = length

    for d in range(4):
        mr, mc = r + dr[d], c + dc[d]
        if 0 <= mr < N and 0 <= mc < N and visited[mr][mc] == 0:

            if arr[r][c] > arr[mr][mc]:
                visited[mr][mc] = 1
                dfs(mr, mc, length + 1, used)
                visited[mr][mc] = 0

            elif not used and arr[mr][mc] - K < arr[r][c]:
                # 공사
                temp = arr[mr][mc]
                arr[mr][mc] = arr[r][c] - 1
                visited[mr][mc] = 1
                dfs(mr, mc, length + 1, True)
                visited[mr][mc] = 0
                arr[mr][mc] = temp


for test_case in range(1, T + 1):
    # N 한 변의 길이, K 최대 공사 가능 깊이
    N, K = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # if test_case != 5:
    #     continue

    max_len = 0

    # 가장 높은 봉우리 높이 찾기
    max_value = -1
    candidate = []
    for r in range(N):
        for c in range(N):
            if max_value <= arr[r][c]:
                max_value = arr[r][c]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_value:
                visited[r][c] = 1
                dfs(r, c, 1, False)
                visited[r][c] = 0

    # max_value = -1
    # start_points = []  # 최고 높이 봉우리 좌표 리스트

    # for r in range(N):
    #     for c in range(N):
    #         if arr[r][c] > max_value:
    #             max_value = arr[r][c]
    #             start_points = [(r, c)]  # 새 최고값이면 초기화
    #         elif arr[r][c] == max_value:
    #             start_points.append((r, c))  # 같은 최고값이면 추가

    #             candidate.append((arr[r][c], r, c))

    # # print(candidate)

    # i = 0
    # while i < len(candidate):
    #     if candidate[i][0] != max_value:
    #         i += 1
    #     else:
    #         break

    # candidate = candidate[i:]
    # for can in candidate:
    #     h, r, c = can
    #     # print(h, r, c)
    #     visited = [[0] * N for _ in range(N)]
    #     visited[r][c] = 1
    #     dfs(r, c, 1, 0)
    #     visited[r][c] = 0

    print(f"#{test_case} {max_len}")

""" 
1
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5

"""
