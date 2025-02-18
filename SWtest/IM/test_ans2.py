T = int(input())  # 테스트 케이스 수

# 델타 배열 : 우, 하, 좌, 상 순서
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())  # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2D 배열 입력

    max_count = 0  # 최대 이동 횟수 저장

    # 모든 좌표에서 시작해보기
    for start_r in range(N):
        for start_c in range(N):
            r, c = start_r, start_c
            count = 1  # 시작점도 포함하므로 1부터 시작

            while True:
                min_value = arr[r][c]
                next_r, next_c = -1, -1

                # 네 방향 탐색
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] < min_value:  # 최소값 비교 (min 함수 사용 안 함)
                            min_value = arr[nr][nc]
                            next_r, next_c = nr, nc

                # 이동할 곳이 없으면 종료
                if next_r == -1 and next_c == -1:
                    break

                # 이동
                r, c = next_r, next_c
                count += 1  # 이동 횟수 증가

            # 최댓값 갱신 (max 함수 사용 안 함)
            if count > max_count:
                max_count = count

    print(f"#{tc} {max_count}")
