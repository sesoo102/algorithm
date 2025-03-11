# 체스판 다시 칠하기

# 체스판 다시 칠하기

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

# 최솟값 초기화
min_value = 64  # 8x8 체스판 전체가 바뀌는 경우가 최대값

# 8×8 체스판을 탐색
for r in range(N - 7):
    for c in range(M - 7):
        black_start = 0  # 'B' 시작 체스판
        white_start = 0  # 'W' 시작 체스판

        for i in range(8):
            for j in range(8):
                # 기준 패턴에 따라 비교
                if (i + j) % 2 == 0:  # 짝수 인덱스 → 'B' 또는 'W' 시작 패턴
                    if chess[r + i][c + j] != "B":
                        black_start += 1  # 'B'여야 하는데 아니면 변경
                    if chess[r + i][c + j] != "W":
                        white_start += 1  # 'W'여야 하는데 아니면 변경
                else:  # 홀수 인덱스 → 'B' 또는 'W' 반대 색
                    if chess[r + i][c + j] != "W":
                        black_start += 1
                    if chess[r + i][c + j] != "B":
                        white_start += 1

        # 최솟값 갱신 (내장 함수 X)
        if black_start < min_value:
            min_value = black_start
        if white_start < min_value:
            min_value = white_start

# 결과 출력
print(min_value)
