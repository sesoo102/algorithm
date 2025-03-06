T = int(input())

for test_case in range(1, T+1):
    # N 세로 크기, M 가로크기
    N, M = list(map(int, input().split()))
    # 배열
    arr = [list(input()) for _ in range(N)]
    code = ''

    for r in range(N):
        for c in range(M, 0, -1):
            if arr[r][c] == 1:
                code = arr[c-55:c+1]
                break
        break
    
    print(code)
    
    