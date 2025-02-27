# 달팽이 숫자

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    r, c, d = 0, 0, 0
    cnt = 1
    arr[r][c] = cnt

    while cnt < N*N:
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] ==0:
            cnt += 1
            arr[nr][nc] = cnt
            r, c = nr, nc
        
        else:
            d = (d+1) % 4
    
    print(f"#{test_case}")
    for row in arr:
        print(" ".join(map(str, row)))