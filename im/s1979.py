# 어디에 단어가 들어갈 수 있을까

T = int(input())


for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for r in range(N):
        word = 0
        for c in range(N):
            if arr[r][c] == 1:
                word += 1
            if arr[r][c] == 0 or c == N-1:
                if word == K:
                    cnt += 1
                word = 0
        
        for c in range(N):
            if arr[c][r] == 1 :
                word += 1
            if arr[c][r] == 0 or c == N-1:
                if word == K:
                    cnt += 1
                word = 0

    print(f"#{test_case} {cnt}")