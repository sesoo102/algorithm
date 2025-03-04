T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    # 2 차원 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 스프레이 가 +, * 형태로 분사. M의 세기로 분사시 각 방향으로 M칸의 파리를 잡을 수 있다.

    #델타를 이용한 2차원 배열

    #상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 대각선
    di2 = [1, 1, -1, -1]
    dj2 = [1, -1, 1, -1]

    max_k = -1  # 최댓값 초기화(최솟값으로 초기화. 근데 최솟값이 왜 -1이야....?
    for r in range(N):
        for c in range(N):
            s1 = arr[r][c]
            s2 = arr[r][c]
            for d in range(4):
                # 상하좌우
                for m in range(1, M):
                    nr = r + di[d]*m
                    nc = c + dj[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        s1 += arr[nr][nc]

                # 대각선
                for m in range(1, M):
                    nr = r + di2[d]*m
                    nc = c + dj2[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        s2 += arr[nr][nc]

            if max_k < s1:
                max_k = s1

            if max_k < s2:
                max_k = s2

    print(f"#{test_case} {max_k}")