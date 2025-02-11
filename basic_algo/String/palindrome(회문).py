# 완전탐색. 가능한 모든 경우 다 구하기.

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))

    txt = [list(input()) for _ in range(N)]


    # 가로 방향 회문 찾기
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if txt[i][j+k] != txt[i][j+M-1-k]:
                    break

            else:
                print(f'#{test_case} {"".join(txt[i][j:j+M])}')
                break



    # 세로 방향 회문 찾기
    for i in range(N-M+1):
        for j in range(N):
            for k in range(M//2):
                if txt[i + k][j] != txt[i + M - 1 - k][j]:
                    break

            else:
                print(f'#{test_case} {"".join(txt[i + k][j] for k in range(M))}')
                break

