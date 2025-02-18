T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):

            # 시작점 arr[r][c]
            count = 0
            # while true/ 재귀함수
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    # 델타 4방향 중 최소값
                    d_min = 0
                    if arr[r + dr[d_min]][c + dc[d_min]] > arr[r + dr[d]][c + dc[d]]:
                        d_min = d
                        if arr[r][c] > arr[r + dr[d_min]][c + dc[d_min]]:
                            r, c = r +dr[d_min][c + dc[d_min]]

    
    # max count값 출력
