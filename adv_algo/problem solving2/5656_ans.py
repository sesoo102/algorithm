from collections import deque

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 구슬이 떨어지는 위치 찾기
def find_target(arr, W, H, col):
    for row in range(H):
        if arr[row][col] > 0:  # 벽돌이 있는 첫 번째 위치 반환
            return row, col
    return -1, -1  # 해당 열에 벽돌이 없는 경우


# 연쇄작용 (벽돌 깨기)
def bomb(arr, W, H, r, c):
    if arr[r][c] == 0:
        return

    q = deque()
    q.append((r, c, arr[r][c]))  # (행, 열, 벽돌 숫자)
    arr[r][c] = 0  # 맞은 벽돌 제거

    while q:
        sr, sc, power = q.popleft()
        for d in range(4):  # 상하좌우 탐색
            for p in range(1, power):
                tr, tc = sr + dr[d] * p, sc + dc[d] * p
                if 0 <= tr < H and 0 <= tc < W and arr[tr][tc] > 0:
                    q.append((tr, tc, arr[tr][tc]))
                    arr[tr][tc] = 0  # 연쇄된 벽돌 제거


# 중력 작용
def apply_gravity(arr, W, H):
    for c in range(W):
        idx = H - 1  # 벽돌이 내려갈 위치
        for r in range(H - 1, -1, -1):
            if arr[r][c]:  # 벽돌이 있으면 아래로 이동
                arr[r][c], arr[idx][c] = arr[idx][c], arr[r][c]
                idx -= 1


# 백트래킹을 이용한 최적해 탐색
def backtrack(cnt, arr, W, H):
    global min_blocks

    # 현재 남은 벽돌 개수 계산 (sum 제거)
    remaining = 0
    for row in arr:
        for x in row:
            if x > 0:
                remaining += 1

    # 모든 구슬을 사용했거나 벽돌이 없는 경우
    if cnt == N or remaining == 0:
        if remaining < min_blocks:
            min_blocks = remaining
        return

    for col in range(W):
        # 현재 상태 저장 (깊은 복사)
        copy_arr = [row[:] for row in arr]

        # 구슬 떨어뜨리기
        r, c = find_target(copy_arr, W, H, col)
        if r == -1:  # 벽돌이 없으면 넘어감
            continue

        bomb(copy_arr, W, H, r, c)  # 벽돌 깨기
        apply_gravity(copy_arr, W, H)  # 중력 작용

        # 다음 구슬 쏘기
        backtrack(cnt + 1, copy_arr, W, H)


# 입력 처리
T = int(input())

for test_case in range(1, T + 1):
    # N: 구슬 쏠 횟수, W: 가로, H: 세로
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    # 최소 남은 벽돌 개수
    min_blocks = 99999  # 초기 큰 값 설정

    # 백트래킹 탐색 시작
    backtrack(0, arr, W, H)

    # 결과 출력
    print(f"#{test_case} {min_blocks}")
