# 파이프 옮기기 1

'''
각 경우를 재귀로 구현
1. 가로
2. 세로
3. 대각선

가로로 갈 수 있는 건 가로, 대각선
세로로 갈 수 있는 건 세로, 대각선
대각선으로 갈 수 있는 건 가로, 세로, 대각선

 각 경우의 좌표로 벽인지 아닌지 판단하고, 범위를 넘어가는지 체크 후 재귀 실행
'''

def move(r, c, direction):
    global ans

    if r == N - 1 and c == N - 1:
        ans += 1
        return

    # 가로 방향으로 이동
    if direction == 0 or direction == 2:
        if c + 1 < N and arr[r][c + 1] == 0:
            move(r, c + 1, 0)

    # 세로 방향으로 이동
    if direction == 1 or direction == 2:
        if r + 1 < N and arr[r + 1][c] == 0:
            move(r + 1, c, 1)

    # 대각선으로 이동
    if r + 1 < N and c + 1 < N:
        if arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
            move(r + 1, c + 1, 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
if arr[N - 1][N - 1] == 1:
    print(0)
else:
    move(0, 1, 0)
    print(ans)
